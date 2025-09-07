import { createIcons, icons } from 'lucide';
import Alpine from 'alpinejs'

window.Alpine = Alpine

Alpine.start()

document.addEventListener('DOMContentLoaded', () => {
  createIcons({ icons });
});