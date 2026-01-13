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


document.addEventListener("DOMContentLoaded", function () {
    const visaCheckbox = document.getElementById("id_need_visa");

    const visaFieldNames = [
        "passport_expiry_date",
        "education_degree",
        "education_institute",
        "specialization",
        "diploma_scan" // ← ДОБАВИЛИ
    ];

    function toggleVisaFields() {
        visaFieldNames.forEach(name => {
            const input = document.querySelector(`[name="${name}"]`);
            if (!input) return;

            const wrapper = input.closest(".profile__field");
            if (!wrapper) return;

            if (visaCheckbox.checked) {
                wrapper.style.display = "";
                input.disabled = false;
            } else {
                wrapper.style.display = "none";
                input.disabled = true;
            }
        });
    }

    toggleVisaFields();
    visaCheckbox.addEventListener("change", toggleVisaFields);
});
