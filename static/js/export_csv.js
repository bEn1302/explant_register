document.addEventListener("DOMContentLoaded", function() {
    // Handler für den Klick auf den Export-Button für Hüftexplantate
    document.getElementById("exportCsvHuefte").addEventListener("click", function(event) {
        event.preventDefault(); // Standardverhalten des Buttons verhindern
        
        // Array zur Sammlung der ausgewählten IDs
        var selectedIds = [];
        
        // Checken Sie, ob die Tabelle die Klasse 'huefte' hat, um die Checkbox-Klasse zu bestimmen
        var className = document.querySelector('#explant-table').classList.contains('huefte') ? 'huefte-row-checkbox' : 'knie-row-checkbox';
        
        // Checkboxen zur Sammlung der ausgewählten IDs
        var checkboxes = document.querySelectorAll('.' + className + ':checked');
        
        // IDs von ausgewählten Checkboxen sammeln
        checkboxes.forEach(function(checkbox) {
            selectedIds.push(checkbox.value);
        });
        
        // Überprüfen, ob mindestens ein Datensatz ausgewählt wurde
        if (selectedIds.length > 0) {
            // URL für den CSV-Export erstellen und die ausgewählten IDs als Parameter hinzufügen
            var exportUrl = "{% url 'explant_csv' %}?selected_ids=" + selectedIds.join("&selected_ids=");
            
            // Weiterleitung zur URL für den CSV-Export
            window.location.href = exportUrl;
        } else {
            // Benutzer über fehlende Auswahl informieren
            alert("Bitte wählen Sie mindestens einen Datensatz aus.");
        }
    });
    
    // Handler für den Klick auf den Export-Button für Knieexplantate
    document.getElementById("exportCsvKnie").addEventListener("click", function(event) {
        event.preventDefault(); // Standardverhalten des Buttons verhindern
        
        // Array zur Sammlung der ausgewählten IDs
        var selectedIds = [];
        
        // Checken Sie, ob die Tabelle die Klasse 'huefte' hat, um die Checkbox-Klasse zu bestimmen
        var className = document.querySelector('#explant-table').classList.contains('huefte') ? 'huefte-row-checkbox' : 'knie-row-checkbox';
        
        // Checkboxen zur Sammlung der ausgewählten IDs
        var checkboxes = document.querySelectorAll('.' + className + ':checked');
        
        // IDs von ausgewählten Checkboxen sammeln
        checkboxes.forEach(function(checkbox) {
            selectedIds.push(checkbox.value);
        });
        
        // Überprüfen, ob mindestens ein Datensatz ausgewählt wurde
        if (selectedIds.length > 0) {
            // URL für den CSV-Export erstellen und die ausgewählten IDs als Parameter hinzufügen
            var exportUrl = "{% url 'explant_csv' %}?selected_ids=" + selectedIds.join("&selected_ids=");
            
            // Weiterleitung zur URL für den CSV-Export
            window.location.href = exportUrl;
        } else {
            // Benutzer über fehlende Auswahl informieren
            alert("Bitte wählen Sie mindestens einen Datensatz aus.");
        }
    });
});