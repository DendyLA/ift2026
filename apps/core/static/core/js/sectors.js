document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.sectors__item');

    items.forEach(item => {
        const popup = item.querySelector('.sectors__popup');
        const closeBtn = popup.querySelector('.sectors__close');

        // открыть по клику на айтем
        item.addEventListener('click', (e) => {
            // если клик был на дескр или на кнопке — не открывать заново
            if (!e.target.closest('.sectors__descr') && !e.target.classList.contains('sectors__close')) {
                popup.classList.add('active');
            }
        });

        // закрыть по кнопке
        closeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            popup.classList.remove('active');
        });

        // закрыть по клику на фон попапа
        popup.addEventListener('click', (e) => {
            // если клик не внутри дескр или кнопки — закрываем
            if (!e.target.closest('.sectors__descr') && !e.target.classList.contains('sectors__close')) {
                popup.classList.remove('active');
            }
        });
    });
});