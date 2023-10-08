document.addEventListener("DOMContentLoaded", function () {
  // Function to toggle the modal visibility
  function toggleModal(modalId) {
    $(`#${modalId}`).modal("toggle");
  }

  // Function to open a specific modal by ID
  function openModalById(modalId) {
    toggleModal(modalId);
  }

  // Example: Open modal when a button is clicked
  const openModalButtons = document.querySelectorAll(".open-modal-button");
  openModalButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const modalId = this.getAttribute("data-modal-id");
      openModalById(modalId);
    });
  });
});