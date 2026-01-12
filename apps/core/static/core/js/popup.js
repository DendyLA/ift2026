document.addEventListener('DOMContentLoaded', function () {
	const popup = document.getElementById('profile-popup');
	const closeBtn = document.getElementById('close-popup');

	if (!popup) return; // если нет попапа (неавторизованные) — выходим

	// Проверяем sessionStorage: показывать только один раз за сессию
	if (!sessionStorage.getItem('profilePopupShown')) {
		popup.style.display = 'flex'; // показать попап
	}

	// Закрытие по крестику
	closeBtn.addEventListener('click', function () {
		popup.style.display = 'none';
		sessionStorage.setItem('profilePopupShown', 'true');
	});

	// Закрытие по клику на оверлей
	popup.addEventListener('click', function (e) {
		if (e.target === popup) {
		popup.style.display = 'none';
		sessionStorage.setItem('profilePopupShown', 'true');
		}
	});
});
