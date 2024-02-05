document.addEventListener("DOMContentLoaded", function() {
    // Handler für den Klick auf den Export-Button
    document.getElementById("exportButton").addEventListener("click", function(event) {
        // Array zum Sammeln der ausgewählten IDs
        var selectedIds = [];
        
        // Überprüfen Sie jede Checkbox und sammeln Sie die ausgewählten IDs
        document.querySelectorAll(".table-row input[type='checkbox']:checked").forEach(function(checkbox) {
            selectedIds.push(checkbox.value);
        });
        
        // Überprüfen, ob mindestens ein Datensatz ausgewählt wurde
        if (selectedIds.length > 0) {
            // Erstellen Sie den URL für den CSV-Export und fügen Sie die ausgewählten IDs als Parameter hinzu
            var exportUrl = "{% url 'explant_csv' %}?selected_ids=" + selectedIds.join("&selected_ids=");
            
            // Weiterleitung zum CSV-Export-URL
            window.location.href = exportUrl;
        } else {
            // Benutzer über fehlende Auswahl informieren
            alert("Bitte wählen Sie mindestens einen Datensatz aus.");
        }
    });
});