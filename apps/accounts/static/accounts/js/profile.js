document.addEventListener('DOMContentLoaded', () => {
    const MAX_SIZE = 15 * 1024 * 1024; // 15 MB

    /* =======================
       POPUP
    ======================= */
    const popup = document.getElementById('fileErrorPopup');
    const popupText = document.getElementById('fileErrorText');
    const popupClose = popup?.querySelector('.file-popup__close');

    function showPopup(message) {
        if (!popup || !popupText) return;

        popupText.textContent = message;
        popup.classList.add('show');

        setTimeout(() => {
            popup.classList.remove('show');
        }, 5000);
    }

    popupClose?.addEventListener('click', () => {
        popup.classList.remove('show');
    });

    /* =======================
       FILE SIZE VALIDATION
    ======================= */
    document.querySelectorAll('input[type="file"]').forEach(input => {
        input.addEventListener('change', function () {
            if (!this.files.length) return;

            const file = this.files[0];

            if (file.size > MAX_SIZE) {
                showPopup('File is too large. Maximum allowed size is 15 MB.');
                this.value = '';
                return;
            }

            // Фото-превью ТОЛЬКО если это фото и размер ок
            if (this.id === 'id_photo') {
                const photoPreview = document.getElementById('photoPreview');
                if (!photoPreview) return;

                const reader = new FileReader();
                reader.onload = e => {
                    photoPreview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    /* =======================
       VISA TOGGLE
    ======================= */
    const visaCheckbox = document.getElementById('id_need_visa');

    if (visaCheckbox) {
        const visaFieldNames = [
            'passport_expiry_date',
            'education_degree',
            'education_institute',
            'specialization',
            'diploma_scan'
        ];

        function toggleVisaFields() {
            visaFieldNames.forEach(name => {
                const input = document.querySelector(`[name="${name}"]`);
                const wrapper = input?.closest('.profile__field');

                if (!input || !wrapper) return;

                if (visaCheckbox.checked) {
                    wrapper.style.display = '';
                    input.disabled = false;
                } else {
                    wrapper.style.display = 'none';
                    input.disabled = true;
                    input.value = '';
                }
            });
        }

        toggleVisaFields();
        visaCheckbox.addEventListener('change', toggleVisaFields);
    }
});
