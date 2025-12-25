document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("userMenuBtn");
    const dropdown = document.getElementById("userDropdown");

    btn.addEventListener("click", (e) => {
        e.stopPropagation();
        dropdown.classList.toggle("is-open");
    });

    document.addEventListener("click", () => {
        dropdown.classList.remove("is-open");
    });
});