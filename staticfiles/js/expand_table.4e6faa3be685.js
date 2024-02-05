document.addEventListener("DOMContentLoaded", function () {
    const triggerCells = document.querySelectorAll(".trigger-cell");

    triggerCells.forEach((cell) => {
      // Create an icon element and add it to the cell
      const icon = document.createElement("i");
      icon.classList.add("bi", "bi-eye");
      cell.appendChild(icon);

      cell.addEventListener("click", function () {
        const extendedRow = this.closest(".table-row").nextElementSibling;

        // Toggle the visibility of the extended row
        extendedRow.classList.toggle("d-none");

        // Toggle the class of the icon to change its appearance
        icon.classList.toggle("bi-eye");
        icon.classList.toggle("bi-eye-slash");
      });
    });
  });