// импорт функции
import { lazyLoadImages } from './lazyLoad.js';

document.addEventListener('DOMContentLoaded', () => {
    lazyLoadImages('.lazy-image', { threshold: 0.7 });
});
