document.addEventListener("DOMContentLoaded", function() {
    // Handler for the click on the export button for Hüftexplantate
    document.getElementById("exportCsvHuefte").addEventListener("click", function(event) {
        handleExport(event, '.huefte-row-checkbox');
    });
    
    // Handler for the click on the export button for Knieexplantate
    document.getElementById("exportCsvKnie").addEventListener("click", function(event) {
        handleExport(event, '.knie-row-checkbox');
    });
});

function handleExport(event, checkboxClass) {
    event.preventDefault(); // Prevent the default behavior of the button
    
    // Array to collect the selected IDs
    var selectedIds = [];
    
    // Checkbox selector based on the provided checkbox class
    var checkboxes = document.querySelectorAll(checkboxClass + ':checked');
    
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
}