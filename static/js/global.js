// импорт функции
import { lazyLoadImages } from './lazyLoad.js';

document.addEventListener('DOMContentLoaded', () => {
    lazyLoadImages('.lazy-image', { threshold: 0.7 });
});



document.addEventListener('DOMContentLoaded', () => {
    // Получаем префикс языка из URL
    const pathParts = window.location.pathname.split('/');
    const langCode = pathParts[1]; // первый сегмент после /

    const supportedLanguages = ['en', 'ru']; // твои языки
    if (supportedLanguages.includes(langCode)) {
        // Устанавливаем cookie django_language на текущий язык
        document.cookie = `django_language=${langCode}; path=/`;
    }
});
