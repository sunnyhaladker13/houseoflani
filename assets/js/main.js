document.addEventListener("DOMContentLoaded", () => {
  // --- Mobile Menu Toggle ---
  const mobileToggle = document.querySelector(".mobile-menu-toggle");
  const nav = document.querySelector(".main-nav");

  if (mobileToggle && nav) {
    mobileToggle.addEventListener("click", () => {
      nav.classList.toggle("active");
      mobileToggle.classList.toggle("active");
    });
  }
});
