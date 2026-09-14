// const isLocalDevelopmentPage =
//   window.location.hostname === "localhost" &&
//   window.location.port !== "5000";

// const API_URL =
//   window.location.protocol === "file:" ||
//     isLocalDevelopmentPage
//     ? "http://localhost:5000/api"
//     : "/api";

// async function submitContactForm(event) {
//   event.preventDefault();
//   const form = event.currentTarget;
//   const button = form.querySelector("button");
//   const status = form.querySelector(".form-status");
//   button.disabled = true;
//   button.textContent = "Sending...";
//   status.textContent = "";
//   try {
//     const response = await fetch(`${API_URL}/contact`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(Object.fromEntries(new FormData(form))) });
//     const responseText = await response.text();
//     let result = {};

//     if (responseText.trim()) {
//       try {
//         result = JSON.parse(responseText);
//       } catch {
//         result = {};
//       }
//     }

//     if (!response.ok) {
//       if (response.status === 405) {
//         throw new Error(
//           "This page is using an old frontend server. Open http://localhost:5000/#contact and try again."
//         );
//       }

//       throw new Error(
//         result.message ||
//         `The server could not process the inquiry (HTTP ${response.status}).`
//       );
//     }

//     status.className = "form-status success-message";
//     status.textContent = result.message || "Your inquiry has been received.";
//     form.reset();
//   } catch (error) {
//     status.className = "form-status error-message";
//     status.textContent = error.name === "TypeError"
//       ? "The contact service is offline. Start the backend and try again."
//       : (error.message || "Something went wrong. Please try again.");
//   } finally {
//     button.disabled = false;
//     button.textContent = "Send Inquiry";
//   }
// }

function closeMenu() {
  document.querySelector(".nav-links")?.classList.remove("open");
  document.querySelector(".menu-toggle")?.setAttribute("aria-expanded", "false");
}

document.querySelector(".menu-toggle").addEventListener("click", () => {
  const menu = document.querySelector(".nav-links");
  const button = document.querySelector(".menu-toggle");
  const open = menu.classList.toggle("open");
  button.setAttribute("aria-expanded", String(open));
});

// Header/footer nav links are present on every full page load now (Django
// renders them server-side), so this only needs to run once per page load
// instead of being re-attached after every route change.
document.querySelectorAll("[data-route]").forEach((element) => element.addEventListener("click", closeMenu));

// The contact form only exists on the contact page, so guard for its absence.
// const contactForm = document.getElementById("contact-form");
// if (contactForm) contactForm.addEventListener("submit", submitContactForm);
