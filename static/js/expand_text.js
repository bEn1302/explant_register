document.addEventListener("DOMContentLoaded", function () {
    const triggerCells = document.querySelectorAll(".trigger-text-cell");

    triggerCells.forEach((cell) => {
        cell.addEventListener("click", function () {
            const fullText = this.getAttribute("data-full-text");
            if (this.textContent.trim() === fullText) {
                this.textContent = fullText.substring(0, 15) + " ...";
            } else {
                this.textContent = fullText;
            }
        });
    });
});
