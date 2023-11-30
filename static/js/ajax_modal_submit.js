function handleAjaxFormSubmit(form, modalId, successCallback) {
    $.ajax({
        type: form.attr('method'),
        url: form.data('url'),
        data: form.serialize(),
        success: function (data) {
            if (data.success) {
                // Erfolgreich hinzugefügt - schließe das Modal oder mach hier etwas nach Bedarf
                $('#' + modalId).modal('hide');
                if (successCallback) {
                    successCallback(data);
                }
            } else {
                // Fehler beim Hinzufügen - zeige Fehlermeldungen an
                $('#alert-container').html('<div class="alert alert-danger">' + data.errors + '</div>');
            }
        },
        error: function () {
            // AJAX-Anfragefehler
            alert('Ein Fehler ist aufgetreten. Bitte versuche es erneut.');
        }
    });
}

$(document).ready(function () {
    $('#addLagerortButton').click(function () {
        var form = $('#addLagerortForm');
        handleAjaxFormSubmit(form, 'addLagerortModal', function (data) {
            // Beispiel: Leere das Formularfeld für Lagerort
            $('#id_lagerort').val('');
            // Hier kannst du weitere Anpassungen nach einem erfolgreichen Hinzufügen vornehmen
        });
    });

    // Füge ähnliche Event-Listener für andere Modals hinzu
    // Beispiel:
    // $('#addPatientButton').click(function () {
    //     var form = $('#addPatientForm');
    //     handleAjaxFormSubmit(form, 'addPatientModal', function (data) {
    //         // Weitere Anpassungen für das Patienten-Modal
    //     });
    // });
});
