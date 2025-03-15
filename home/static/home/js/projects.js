function filterProjects(category) {
    const cards = document.querySelectorAll('.project-card');
  
    cards.forEach(card => {
      if (category === 'all' || card.classList.contains(category)) {
        card.classList.remove('hidden');
        card.classList.add('block');
        setTimeout(() => card.classList.add('opacity-100'), 10);
        card.classList.remove('opacity-0');
      } else {
        card.classList.remove('opacity-100');
        card.classList.add('opacity-0');
        setTimeout(() => {
          card.classList.add('hidden');
          card.classList.remove('block');
        }, 300);
      }
    });
  }
  
  function openModal(title, description, imageUrl, githubLink, liveDemoLink) {
    const modal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContent');
  
    modal.classList.remove('hidden', 'pointer-events-none', 'opacity-0');
    modal.classList.add('flex', 'opacity-100');
  
    setTimeout(() => {
      modalContent.classList.remove('scale-95');
      modalContent.classList.add('scale-100');
    }, 50);
  
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDescription').innerText = description;
    document.getElementById('modalImage').src = imageUrl;
  
    const githubBtn = document.getElementById('modalGithub');
    const liveDemoBtn = document.getElementById('modalLive');
  
    githubBtn.href = githubLink || '#';
    githubBtn.classList.toggle('hidden', !githubLink);
  
    liveDemoBtn.href = liveDemoLink || '#';
    liveDemoBtn.classList.toggle('hidden', !liveDemoLink);
  }
  
  function closeModal() {
    const modal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContent');
  
    modal.classList.add('opacity-0');
    modal.classList.remove('opacity-100');
  
    modalContent.classList.add('scale-95');
    modalContent.classList.remove('scale-100');
  
    setTimeout(() => {
      modal.classList.remove('flex');
      modal.classList.add('hidden', 'pointer-events-none');
    }, 300);
  }
  