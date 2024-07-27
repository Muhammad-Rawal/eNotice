document.addEventListener("DOMContentLoaded", function () {
  const userMenuButton = document.getElementById("user-menu-button");
  const userDropdown = document.getElementById("user-dropdown");

  // Toggle dropdown visibility
  userMenuButton.addEventListener("click", function () {
    const isOpen = userDropdown.classList.contains("hidden");
    userDropdown.classList.toggle("hidden", !isOpen);
    userMenuButton.setAttribute("aria-expanded", String(!isOpen));
  });

  // Close dropdown if user clicks outside of it
  document.addEventListener("click", function (event) {
    if (
      !userMenuButton.contains(event.target) &&
      !userDropdown.contains(event.target)
    ) {
      userDropdown.classList.add("hidden");
      userMenuButton.setAttribute("aria-expanded", "false");
    }
  });
});
