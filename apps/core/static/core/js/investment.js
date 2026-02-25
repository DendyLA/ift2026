document.querySelectorAll('.investment__item').forEach(item => {

    const hoverImage = item.dataset.hover;
    if (!hoverImage) return;

    const layer = document.createElement('div');
    layer.classList.add('hover-layer');
    layer.style.backgroundImage = `url(${hoverImage})`;
    item.appendChild(layer);

    let entered = false;

    item.addEventListener('mouseenter', e => {
        const rect = item.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        // стартуем из точки входа
        layer.style.transition = 'none';
        layer.style.clipPath = `circle(0px at ${x}px ${y}px)`;

        // принудительный reflow
        layer.offsetHeight;

        // анимируем раскрытие
        layer.style.transition = 'clip-path 0.3s ease';
        layer.style.clipPath = `circle(120px at ${x}px ${y}px)`;

        entered = true;
    });

    item.addEventListener('mousemove', e => {
        if (!entered) return;

        const rect = item.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        layer.style.clipPath = `circle(120px at ${x}px ${y}px)`;
    });

    item.addEventListener('mouseleave', e => {
        const rect = item.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        layer.style.clipPath = `circle(0px at ${x}px ${y}px)`;
        entered = false;
    });

});