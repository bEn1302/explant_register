// Funktion, um alle Checkboxen zu aktivieren/deaktivieren
function toggleCheckboxes(checked) {
    var checkboxes = document.querySelectorAll('.row-checkbox');
    checkboxes.forEach(function (checkbox) {
    checkbox.checked = checked;
    });
}

// Hör auf Änderungen an der "Select All"-Checkbox
document.getElementById('selectAll').addEventListener('change', function () {
    toggleCheckboxes(this.checked);
});

// Hör auf Klick-Ereignisse auf den Tabelleneinträgen
var rowCheckboxes = document.querySelectorAll('.row-checkbox');
rowCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
    // Hier kannst du die gewünschte Aktion ausführen, z.B. wenn eine Checkbox ausgewählt wird
    if (this.checked) {
        // Führe deine Aktion aus
        console.log('Checkbox ausgewählt: ' + this.parentNode.parentNode.innerText);
    }
    });
});
