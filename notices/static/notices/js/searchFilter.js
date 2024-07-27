document.addEventListener("DOMContentLoaded", function () {
  // Search functionality
  const searchInput = document.getElementById("table-search");
  searchInput.addEventListener("input", function () {
    const searchText = this.value.trim().toLowerCase();
    const rows = document.querySelectorAll("#notices-table tbody tr");
    rows.forEach((row) => {
      const title = row
        .querySelector("td:first-child")
        .textContent.trim()
        .toLowerCase();
      if (title.includes(searchText)) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  });

  // Filter by Date functionality
  const filterRadios = document.querySelectorAll(".filter-radio");
  filterRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      const days = parseInt(this.value);
      const currentDate = new Date();
      const cutoffDate = new Date(
        currentDate.getTime() - days * 24 * 60 * 60 * 1000
      );
      const rows = document.querySelectorAll("#notices-table tbody tr");
      rows.forEach((row) => {
        const postedAt = new Date(
          row.querySelector("td:nth-child(3)").textContent
        );
        if (postedAt >= cutoffDate) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  });

  // Toggle dropdown menu
  const dropdownToggleButton = document.getElementById("dropdownRadioButton");
  const dropdownMenu = document.getElementById("dropdownRadio");
  dropdownToggleButton.addEventListener("click", function () {
    dropdownMenu.classList.toggle("hidden");
  });
});
