document.addEventListener('DOMContentLoaded', function () {
    const photoInput = document.getElementById('id_photo');
    const photoPreview = document.getElementById('photoPreview');

    photoInput.addEventListener('change', function (event) {
        const file = event.target.files[0]; // первый файл из input
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                photoPreview.src = e.target.result; // сразу меняем src на выбранный файл
            };
            reader.readAsDataURL(file);
        }
    });
});
