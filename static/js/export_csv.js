document.addEventListener("DOMContentLoaded", function() {
    // Handler for the click on the export button
    document.getElementById("exportButton").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default behavior of the button
        
        // Array to collect the selected IDs
        var selectedIds = [];
        
        // Check if the table contains class 'huefte' or 'knie' to determine the checkbox class
        var className = document.querySelector('#explant-table').classList.contains('huefte') ? 'huefte-row-checkbox' : 'knie-row-checkbox';
        
        // Checkboxes to gather selected IDs
        var checkboxes = document.querySelectorAll('.' + className + ':checked');
        
        // Collect IDs from selected checkboxes
        checkboxes.forEach(function(checkbox) {
            selectedIds.push(checkbox.value);
        });
        
        // Check if at least one dataset is selected
        if (selectedIds.length > 0) {
            // Create the URL for the CSV export and add the selected IDs as parameters
            var exportUrl = "{% url 'explant_csv' %}?selected_ids=" + selectedIds.join("&selected_ids=");
            
            // Redirect to the CSV export URL
            window.location.href = exportUrl;
        } else {
            // Notify the user about the lack of selection
            alert("Bitte wählen Sie mindestens einen Datensatz aus.");
        }
    });
});