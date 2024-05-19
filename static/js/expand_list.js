document.addEventListener("DOMContentLoaded", function() {
    var listItemsWithSubitems = document.querySelectorAll('.list-group-item');

    listItemsWithSubitems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            var subItems = this.querySelector('ul');
            var icon = this.querySelector('.toggle-subitems');
            if (subItems) {
                var isExpanded = (subItems.style.display === 'block');
                subItems.style.display = isExpanded ? 'none' : 'block';
                if (icon) {
                    icon.className = isExpanded ? 'bi bi-chevron-right me-2 toggle-subitems' : 'bi bi-chevron-down me-2 toggle-subitems';
                }
            }
        });

        // Prevent the sublist items from collapsing the list when clicked
        var sublistAnchors = item.querySelectorAll('.sublist a');
        sublistAnchors.forEach(function(anchor) {
            anchor.addEventListener('click', function(event) {
                event.stopPropagation();
            });
        });
    });
});