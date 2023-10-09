$(document).ready(function() {
    // AJAX-Anfrage beim Klicken auf den "Speichern"-Button im Modal
    $('#update-form').submit(function(e) {
        e.preventDefault(); // Verhindert das Standardverhalten des Formulars

        var form = $(this);
        
        $.ajax({
            type: 'POST',
            url: form.attr('action'), // Verwenden Sie den action-Wert aus dem Formular
            data: form.serialize(),
            success: function(data) {
                if (data.success) {
                    // Erfolgreiche Aktualisierung, zeige Erfolgsmeldung im Modal
                    $('#alert-container').html('<div class="alert alert-success" role="alert">Erfolgreich aktualisiert.</div>');
                } else {
                    // Fehler beim Formular, zeige Fehlermeldung im Modal
                    $('#alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Aktualisieren.</div>');
                }
            }
        });
    });
});
