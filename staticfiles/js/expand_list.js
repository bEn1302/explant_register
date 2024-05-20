document.addEventListener("DOMContentLoaded", function() {
    var toggleIcons = document.querySelectorAll('.toggle-subitems');

    toggleIcons.forEach(function(icon) {
        icon.addEventListener('click', function(event) {
            event.stopPropagation();

            var subItems = this.parentElement.nextElementSibling.querySelector('.sublist');
            if (subItems) {
                var isExpanded = (subItems.style.display === 'block');
                subItems.style.display = isExpanded ? 'none' : 'block';
                this.className = isExpanded ? 'bi bi-chevron-right me-2 toggle-subitems' : 'bi bi-chevron-down me-2 toggle-subitems';
            }
        });
    });

    var sublistAnchors = document.querySelectorAll('.sublist a');
    sublistAnchors.forEach(function(anchor) {
        anchor.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    });
});