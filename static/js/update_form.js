$(document).ready(function() {
    $('form[id^="update-form"]').submit(function(e) {
        e.preventDefault(); // Verhindert das Standardverhalten des Formulars

        var form = $(this);
        var targetModalId = form.attr('data-bs-target'); // Zielmodal aus dem Formular holen

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form.serialize(),
            success: function(data) {
                if (data.success) {
                    $(targetModalId).modal('hide'); // Das entsprechende Modal schließen

                    // Erfolgreiche Aktualisierung, zeige Erfolgsmeldung im entsprechenden Modal
                    $(targetModalId + ' .modal-body #alert-container').html('<div class="alert alert-success" role="alert">Reoperation erfolgreich aktualisiert.</div>');
                } else {
                    // Fehler beim Formular, zeige Fehlermeldung im entsprechenden Modal
                    $(targetModalId + ' .modal-body #alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Aktualisieren der Reoperation.</div>');
                }
            }
        });
    });
});