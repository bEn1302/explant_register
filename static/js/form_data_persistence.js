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
    $('#add-explant').on('click', function (event) {
        // Entferne die gespeicherten Daten aus dem Local Storage
        localStorage.removeItem('ursache');
        localStorage.removeItem('verfuegbarkeit');
        localStorage.removeItem('herkunftsort');
        localStorage.removeItem('entnahme_datum');
        localStorage.removeItem('eingang_datum');
        localStorage.removeItem('bruchgeschehen');
        localStorage.removeItem('nutzungsdauer');
        localStorage.removeItem('reinigung');
        localStorage.removeItem('entnahme_datum');
        localStorage.removeItem('eingang_datum');
        localStorage.removeItem('lagerort');
        localStorage.removeItem('patient');
        localStorage.removeItem('reoperation');
        localStorage.removeItem('inlay');
        localStorage.removeItem('kopf');
        localStorage.removeItem('femurkomponente');
        localStorage.removeItem('schaft');
        localStorage.removeItem('tibiaplateau');
        localStorage.removeItem('pfanne');
        localStorage.removeItem('patellaersatz');
    });    
});