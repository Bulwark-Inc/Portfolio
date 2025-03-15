document.addEventListener('DOMContentLoaded', () => {
    const darkToggleBtn = document.getElementById('darkToggleBtn');
    const htmlElement = document.documentElement;

    // Check saved preference
    if (localStorage.getItem('theme') === 'dark') {
        htmlElement.classList.add('dark');
        darkToggleBtn.setAttribute('aria-pressed', true);
        darkToggleBtn.innerHTML = '☀️';
    }

    darkToggleBtn.addEventListener('click', toggleDarkMode);

    function toggleDarkMode() {
        htmlElement.classList.add('transitioning');
        document.body.style.opacity = '0.5';

        setTimeout(() => {
            htmlElement.classList.toggle('dark');
            const isDark = htmlElement.classList.contains('dark');

            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            darkToggleBtn.setAttribute('aria-pressed', isDark);
            darkToggleBtn.innerHTML = isDark ? '☀️' : '🌙';

            document.body.style.opacity = '1';
        }, 200);
    }
});
