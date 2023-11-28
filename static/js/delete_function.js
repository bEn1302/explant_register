document.addEventListener("DOMContentLoaded", function() {
    var deleteButtons = document.querySelectorAll('.deleteButton');
    
    deleteButtons.forEach(function(deleteButton) {
        deleteButton.addEventListener('click', function() {
            var form = deleteButton.closest('form');
            if (form) {
                if (confirm("Are you sure you want to delete the selected explantate(s)?")) {
                    form.submit();
                }
            } else {
                console.error('Form element not found.');
            }
        });
    });
});