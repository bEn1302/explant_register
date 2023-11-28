document.addEventListener("DOMContentLoaded", function() {
    // Finde den Delete-Button
    var deleteButton = document.getElementById('deleteButton');

    // Füge einen Event Listener hinzu
    deleteButton.addEventListener('click', function() {
        // Finde alle Checkboxen je nachdem, ob es sich um Hüfte oder Knie handelt
        var checkboxes = document.querySelectorAll('.table-row input[type="checkbox"]:checked');
        
        // Iteriere über die ausgewählten Checkboxen
        checkboxes.forEach(function(checkbox) {
            // Finde die Zeile (TR) der Checkbox
            var row = checkbox.closest('tr');
            
            // Entferne die Zeile aus der Tabelle
            row.parentNode.removeChild(row);
        });
    });
});