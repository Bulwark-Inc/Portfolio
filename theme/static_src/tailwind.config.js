/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
/** @type {import('tailwindcss').Config} */

module.exports = {
    darkMode: 'class',
    content: [
        '../../templates/**/*.html',
        '../../home/templates/**/*.html',        
        '../../home/static/**/*.js',
    ],
    theme: {
        extend: {
            colors: {
                primary: '#0ea5e9',    // sky-500
                secondary: '#64748b',  // slate-500
                accent: '#10b981',     // emerald-500
                dark: '#0f172a',       // slate-900
              },
              fontFamily: {
                sans: ['Inter', 'ui-sans-serif', 'system-ui'],
              },
              keyframes: {
                fadeIn: {
                  '0%': { opacity: 0 },
                  '100%': { opacity: 1 },
                },
              },
              animation: {
                fadeIn: 'fadeIn 1s ease-out',
              },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
