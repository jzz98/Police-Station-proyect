document.addEventListener("DOMContentLoaded", function () {
  // Alert Modal Functionality
  const viewDetailsButtons = document.querySelectorAll(".view-details");
  const closeModalButtons = document.querySelectorAll(".close-modal");

  viewDetailsButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const alertId = this.getAttribute("data-alert-id");
      const modal = document.getElementById(`alertModal${alertId}`);
      modal.style.display = "block";
      document.body.style.overflow = "hidden";
    });
  });

  closeModalButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const modal = this.closest(".alert-modal");
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    });
  });

  // Close modal when clicking outside of content
  const modals = document.querySelectorAll(".alert-modal");
  modals.forEach((modal) => {
    modal.addEventListener("click", function (e) {
      if (e.target === this) {
        this.style.display = "none";
        document.body.style.overflow = "auto";
      }
    });
  });

  // News Read More functionality
  const readMoreButtons = document.querySelectorAll(".read-more");

  readMoreButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const newsId = this.getAttribute("data-news-id");
      const content = document.getElementById(`news-content-${newsId}`);
      const icon = this.querySelector("i");

      content.classList.toggle("expanded");

      if (content.classList.contains("expanded")) {
        this.querySelector("i").style.transform = "rotate(180deg)";
        this.textContent = "Leer Menos ";
        this.appendChild(icon);
      } else {
        this.querySelector("i").style.transform = "rotate(0)";
        this.textContent = "Leer Más ";
        this.appendChild(icon);
      }
    });
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 100,
          behavior: "smooth",
        });
      }
    });
  });

  // Login/Register Modal Logic
  const modalLogin = document.getElementById("modalLogin");
  const modalRegister = document.getElementById("modalRegister");
  const btnLogin = document.getElementById("btnLogin");
  const btnRegister = document.getElementById("btnRegister");
  const toRegister = document.getElementById("toRegister");
  const toLogin = document.getElementById("toLogin");
  const closeButtons = document.querySelectorAll(".close-modal");

  function openModal(modal) {
    modal.classList.remove("hidden");
    document.body.style.overflow = "hidden";
  }
  function closeModal(modal) {
    modal.classList.add("hidden");
    document.body.style.overflow = "auto";
  }

  btnLogin.addEventListener("click", () => openModal(modalLogin));
  btnRegister.addEventListener("click", () => openModal(modalRegister));

  toRegister.addEventListener("click", () => {
    closeModal(modalLogin);
    openModal(modalRegister);
  });
  toLogin.addEventListener("click", () => {
    closeModal(modalRegister);
    openModal(modalLogin);
  });

  closeButtons.forEach((btn) =>
    btn.addEventListener("click", (e) => {
      const parentModal = e.target.closest(".fixed");
      closeModal(parentModal);
    })
  );

  // Prevent clicks inside modal content from closing
  [modalLogin, modalRegister].forEach((modal) => {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal(modal);
    });
  });

  // Optional: handle form submissions here
});
