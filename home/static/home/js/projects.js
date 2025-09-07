// home/js/projects.js

document.addEventListener('DOMContentLoaded', () => {
    // --- Modal Logic ---
    const projectModal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContent');
    const modalImage = document.getElementById('modalImage');
    const modalTitle = document.getElementById('modalTitle');
    const modalDescription = document.getElementById('modalDescription');
    const modalGithubBtn = document.getElementById('modalGithub');
    const modalLiveBtn = document.getElementById('modalLive');

    // Function to open the modal using a data object
    function openModal(data) {
        modalTitle.innerText = data.title;
        modalDescription.innerText = data.description;
        modalImage.src = data.imageUrl;

        // Toggle button visibility based on whether the links exist
        if (data.githubLink) {
            modalGithubBtn.href = data.githubLink;
            modalGithubBtn.classList.remove('hidden');
        } else {
            modalGithubBtn.classList.add('hidden');
        }

        if (data.liveDemoLink) {
            modalLiveBtn.href = data.liveDemoLink;
            modalLiveBtn.classList.remove('hidden');
        } else {
            modalLiveBtn.classList.add('hidden');
        }

        // Apply classes to open the modal with a smooth transition
        projectModal.classList.remove('opacity-0', 'pointer-events-none');
        projectModal.classList.add('opacity-100');
        modalContent.classList.remove('scale-95');
    }

    // Function to close the modal
    function closeModal() {
        projectModal.classList.remove('opacity-100');
        projectModal.classList.add('opacity-0', 'pointer-events-none');
        modalContent.classList.add('scale-95');
    }

    // Event listener to open modal by clicking on a project card
    document.querySelectorAll('[data-modal-trigger]').forEach(button => {
        button.addEventListener('click', (event) => {
            const card = event.currentTarget.closest('.project-card');
            if (card) {
                const data = card.dataset;
                openModal(data);
            }
        });
    });

    // Event listener to close modal by clicking the close button
    document.querySelector('[data-modal-close]').addEventListener('click', closeModal);

    // Event listener to close modal by clicking outside the content
    projectModal.addEventListener('click', (event) => {
        if (event.target === projectModal) {
            closeModal();
        }
    });

    // --- Project Filtering Logic ---
    const filterButtons = document.querySelectorAll('[data-filter]');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const filterValue = event.target.dataset.filter;
            
            // Update button styles
            filterButtons.forEach(btn => {
                btn.classList.remove('active-filter');
            });
            event.target.classList.add('active-filter');

            // Show/hide cards based on the filter
            projectCards.forEach(card => {
                const category = card.dataset.category;
                if (filterValue === 'all' || category === filterValue) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
});