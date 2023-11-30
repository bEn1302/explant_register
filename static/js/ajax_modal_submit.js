$(document).ready(function () {
    $('.add-button').click(function (e) {
        e.preventDefault();

        var formId = $(this).data('form-id');
        var form = $('#' + formId);

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form.serialize(),
            success: function (data) {
                if (data.success) {
                    // Erfolgreiche Verarbeitung: Hier kannst du das Formular aktualisieren oder eine Benachrichtigung anzeigen.
                    alert('Daten erfolgreich hinzugefügt!');
                    // Beispiel: Formular zurücksetzen
                    form.trigger('reset');
                } else {
                    // Fehler beim Speichern: Hier kannst du Fehler anzeigen oder andere Maßnahmen ergreifen.
                    alert('Fehler beim Hinzufügen der Daten:\n' + JSON.stringify(data.errors));
                }
            },
            error: function () {
                alert('Fehler bei der AJAX-Anfrage');
            }
        });
    });
});