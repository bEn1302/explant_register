$(document).ready(function () {
    // Define an array of field names
    const fields = [
        'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum',
        'bruchgeschehen', 'nutzungsdauer', 'reinigung', 'lagerort', 'patient',
        'reoperation', 'inlay', 'kopf', 'femurkomponente', 'schaft',
        'tibiaplateau', 'pfanne', 'patellaersatz'
    ];

    // Überprüfe, ob lokale Werte gespeichert sind
    fields.forEach(function (field) {
        const value = localStorage.getItem(field);
        if (value !== null) {
            if (field === 'verfuegbarkeit' || field === 'reinigung') {
                $(`#id_${field}`).prop('checked', value === 'true');
            } else {
                $(`#id_${field}`).val(value);
            }
        }
    });

    // Überwache Änderungen und speichere sie lokal
    fields.forEach(function (field) {
        $(`#id_${field}`).on('input change', function () {
            const value = this.type === 'checkbox' ? $(this).prop('checked') : $(this).val();
            localStorage.setItem(field, value);
        });
    });

    // Überwache das Klicken auf den Submit-Button
    $('.add-explant').on('click', function (event) {
        // Entferne die gespeicherten Daten aus dem Local Storage
        fields.forEach(function (field) {
            localStorage.removeItem(`${field}`);
        });
    });    
});