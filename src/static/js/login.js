document.addEventListener("DOMContentLoaded", function () {
  const loginTab = document.getElementById("login-tab");
  const registerTab = document.getElementById("register-tab");
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  const successMessage = document.getElementById("success-message");
  const loadingOverlay = document.getElementById("loading-overlay");
  const successText = document.getElementById("success-text");
  const continueButton = document.getElementById("continue-button");

  // Tab switching functionality
  loginTab.addEventListener("click", function () {
    loginTab.classList.add("tab-active");
    registerTab.classList.remove("tab-active");
    loginForm.classList.remove("hidden");
    registerForm.classList.add("hidden");
    successMessage.classList.add("hidden");
  });

  registerTab.addEventListener("click", function () {
    registerTab.classList.add("tab-active");
    loginTab.classList.remove("tab-active");
    registerForm.classList.remove("hidden");
    loginForm.classList.add("hidden");
    successMessage.classList.add("hidden");
  });

  // Toggle password visibility
  const togglePasswordButtons = document.querySelectorAll(".toggle-password");
  togglePasswordButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const passwordInput = this.parentElement.querySelector("input");
      const icon = this.querySelector("i");

      if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
      } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
      }
    });
  });

  const form = document.getElementById("loginform");
  // Form submission handlers
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Basic validation
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    let isValid = true;

    if (!username || username.length < 3) {
      document
        .getElementById("username")
        .parentElement.querySelector(".error-message")
        .classList.remove("hidden");
      isValid = false;
    } else {
      document
        .getElementById("username")
        .parentElement.querySelector(".error-message")
        .classList.add("hidden");
    }

    if (!password || password.length < 6) {
      document
        .getElementById("password")
        .parentElement.querySelector(".error-message")
        .classList.remove("hidden");
      isValid = false;
    } else {
      document
        .getElementById("password")
        .parentElement.querySelector(".error-message")
        .classList.add("hidden");
    }

    if (isValid) {
      // Show loading overlay
      loadingOverlay.classList.remove("hidden");

      // Simulate API call (to be replaced with actual API)
      setTimeout(() => {
        loadingOverlay.classList.add("hidden");
        loginForm.classList.add("hidden");
        successMessage.classList.remove("hidden");
        successText.textContent =
          "Ha iniciado sesión correctamente en el sistema.";
        form.submit();
      }, 1500);
    }
  });

  document
    .getElementById("registerForm")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      // Basic validation
      const fullname = document.getElementById("fullname").value;
      const username = document.getElementById("reg-username").value;
      const password = document.getElementById("reg-password").value;
      const confirmPassword = document.getElementById(
        "reg-confirm-password"
      ).value;
      const terms = document.getElementById("terms").checked;
      let isValid = true;

      if (!fullname || fullname.length < 3) {
        document
          .getElementById("fullname")
          .parentElement.querySelector(".error-message")
          .classList.remove("hidden");
        isValid = false;
      } else {
        document
          .getElementById("fullname")
          .parentElement.querySelector(".error-message")
          .classList.add("hidden");
      }

      if (!username || username.length < 5) {
        document
          .getElementById("reg-username")
          .parentElement.querySelector(".error-message")
          .classList.remove("hidden");
        isValid = false;
      } else {
        document
          .getElementById("reg-username")
          .parentElement.querySelector(".error-message")
          .classList.add("hidden");
      }

      if (!password || password.length < 8) {
        document
          .getElementById("reg-password")
          .parentElement.querySelector(".error-message")
          .classList.remove("hidden");
        isValid = false;
      } else {
        document
          .getElementById("reg-password")
          .parentElement.querySelector(".error-message")
          .classList.add("hidden");
      }

      if (password !== confirmPassword) {
        document
          .getElementById("reg-confirm-password")
          .parentElement.querySelector(".error-message")
          .classList.remove("hidden");
        isValid = false;
      } else {
        document
          .getElementById("reg-confirm-password")
          .parentElement.querySelector(".error-message")
          .classList.add("hidden");
      }

      if (!terms) {
        document
          .getElementById("terms")
          .parentElement.parentElement.querySelector(".error-message")
          .classList.remove("hidden");
        isValid = false;
      } else {
        document
          .getElementById("terms")
          .parentElement.parentElement.querySelector(".error-message")
          .classList.add("hidden");
      }

      if (isValid) {
        // Show loading overlay
        loadingOverlay.classList.remove("hidden");

        // Simulate API call (to be replaced with actual API)
        setTimeout(function () {
          loadingOverlay.classList.add("hidden");
          registerForm.classList.add("hidden");
          successMessage.classList.remove("hidden");
          successText.textContent = "Su cuenta ha sido creada exitosamente.";
        }, 1500);
      }
    });

  // Continue button handler
  continueButton.addEventListener("click", function () {
    successMessage.classList.add("hidden");
    loginTab.classList.add("tab-active");
    registerTab.classList.remove("tab-active");
    loginForm.classList.remove("hidden");

    // Reset forms
    document.getElementById("loginForm").reset();
    document.getElementById("registerForm").reset();
  });
});
