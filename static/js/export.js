document.addEventListener("DOMContentLoaded", function() {
    // Handler for the click on the export button for Hüftexplantate (PDF)
    document.getElementById("exportPdfHuefte").addEventListener("click", function(event) {
        handleExport(event, '.huefte-row-checkbox', 'pdf', 'huefte');
    });
    
    // Handler for the click on the export button for Knieexplantate (PDF)
    document.getElementById("exportPdfKnie").addEventListener("click", function(event) {
        handleExport(event, '.knie-row-checkbox', 'pdf', 'knie');
    });

    // Handler for the click on the export button for Hüftexplantate (CSV)
    document.getElementById("exportCsvHuefte").addEventListener("click", function(event) {
        handleExport(event, '.huefte-row-checkbox', 'csv');
    });
    
    // Handler for the click on the export button for Knieexplantate (CSV)
    document.getElementById("exportCsvKnie").addEventListener("click", function(event) {
        handleExport(event, '.knie-row-checkbox', 'csv');
    });
});

function handleExport(event, checkboxClass, exportType, type) {
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
        // Create the URL for the export and add the selected IDs as parameters
        var exportUrl = "";
        if (exportType === 'pdf') {
            exportUrl = "/explant_pdf/?selected_ids=" + selectedIds.join("&selected_ids=") + "&type=" + type;
        } else if (exportType === 'csv') {
            exportUrl = "/explant_csv/?selected_ids=" + selectedIds.join("&selected_ids=");
        }
        
        // Redirect to the export URL
        window.location.href = exportUrl;
    } else {
        // Notify the user about the lack of selection
        alert("Please select at least one dataset.");
    }
}
