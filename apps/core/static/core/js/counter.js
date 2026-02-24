document.addEventListener("DOMContentLoaded", function () {
    const registrationEndDate = new Date(2026, 2, 18, 0, 0, 0); // 15 марта 2026

    const daysEl = document.querySelector(".registration-counter .days");
    const hoursEl = document.querySelector(".registration-counter .hours");
    const minutesEl = document.querySelector(".registration-counter .minutes");
    const secondsEl = document.querySelector(".registration-counter .seconds");

    function updateCounter() {
        const now = new Date();
        const diff = registrationEndDate - now;

        if (diff <= 0) {
            daysEl.textContent = 0;
            hoursEl.textContent = 0;
            minutesEl.textContent = 0;
            secondsEl.textContent = 0;
            clearInterval(interval);
            return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        daysEl.textContent = days;
        hoursEl.textContent = hours;
        minutesEl.textContent = minutes;
        secondsEl.textContent = seconds;
    }

    updateCounter();
    const interval = setInterval(updateCounter, 1000);
});