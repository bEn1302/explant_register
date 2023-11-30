function handleFormSubmit(form, modalId, successCallback) {
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (data) {
            if (data.success) {
                $('#' + modalId).modal('hide');
                if (successCallback) {
                    successCallback(data);
                }
            } else {
                $('#alert-container').html('<div class="alert alert-danger">' + data.errors + '</div>');
            }
        },
        error: function () {
            alert('Ein Fehler ist aufgetreten. Bitte versuche es erneut.');
        }
    });
}

function saveFormDataToDB(form) {
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (data) {
            if (data.success) {
                console.log('Daten erfolgreich in der Datenbank gespeichert.');
            } else {
                console.log('Fehler beim Speichern in der Datenbank:', data.errors);
            }
        },
        error: function () {
            console.log('AJAX-Anfragefehler beim Speichern in der Datenbank.');
        }
    });
}

$(document).ready(function () {
    // Generische Funktion zum Hinzufügen von Modal-Formularen
    function addModalForm(formId, modalId, submitButtonId, successCallback) {
        $('#' + submitButtonId).click(function () {
            var form = $('#' + formId);
            handleFormSubmit(form, modalId, successCallback);
            saveFormDataToDB(form);
        });
    }

    // Beispiel für ein Modal-Formular
    addModalForm('addInlayForm', 'addInlayModal', 'addInlayButton', function (data) {
        // Hier kannst du nach einem erfolgreichen Hinzufügen Anpassungen vornehmen
        $('#id_inlay').val('');
    });

    // Füge ähnliche Event-Listener für andere Modal-Formulare hinzu
    addModalForm('addKopfForm', 'addKopfModal', 'addKopfButton', function (data) {
        // Weitere Anpassungen für das Kopf-Modal
        $('#id_kopf').val('');
    });

    // Wiederhole dies für alle Modal-Formulare
    // ...
});
