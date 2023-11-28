document.addEventListener("DOMContentLoaded", function() {
    var deleteButtons = document.querySelectorAll('.deleteButton');
    var deleteForms = document.querySelectorAll('.deleteForm');

    deleteButtons.forEach(function(deleteButton, index) {
        deleteButton.addEventListener('click', function() {
            var form = deleteForms[index];
            if (confirm("Are you sure you want to delete the selected explantate(s)?")) {
                form.submit();
            }
        });
    });
});