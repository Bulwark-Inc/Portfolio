document.addEventListener('DOMContentLoaded', () => {
    const darkToggleBtn = document.getElementById('darkToggleBtn');
    const darkModeIcon = document.getElementById('darkModeIcon');
    const htmlElement = document.documentElement;

    // Set initial icon based on theme
    const isDark = htmlElement.classList.contains('dark');
    darkModeIcon.setAttribute('data-lucide', isDark ? 'sun' : 'moon');
    darkToggleBtn.setAttribute('aria-pressed', isDark);

    darkToggleBtn.addEventListener('click', toggleDarkMode);

    function toggleDarkMode() {
        htmlElement.classList.add('transitioning');
        document.body.style.opacity = '0.5';

        setTimeout(() => {
            htmlElement.classList.toggle('dark');
            const isDark = htmlElement.classList.contains('dark');

            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            darkToggleBtn.setAttribute('aria-pressed', isDark);

            // Change the icon and re-render
            darkModeIcon.setAttribute('data-lucide', isDark ? 'sun' : 'sun');

            document.body.style.opacity = '1';
        }, 200);
    }
});