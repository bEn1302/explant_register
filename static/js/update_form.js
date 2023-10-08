$(document).ready(function() {
    // AJAX-Anfrage beim Klicken auf den "Speichern"-Button im Modal
    $('#lagerortUpdateForm').submit(function(e) {
        e.preventDefault(); // Verhindert das Standardverhalten des Formulars

        var form = $(this);
        
        $.ajax({
            type: 'POST',
            url: form.attr('action'), // Verwenden Sie den action-Wert aus dem Formular
            data: form.serialize(),
            success: function(data) {
                if (data.success) {
                    // Erfolgreiche Aktualisierung, zeige Erfolgsmeldung auf der aktuellen Seite ('explants')
                    $('#alert-container').html('<div class="alert alert-success" role="alert">Lagerort erfolgreich aktualisiert.</div>');

                    // Aktualisiere die Anzeige auf der Seite mit den neuen Daten (falls erforderlich)
                    $('#schrankValue').text(form.find('#schrank').val());
                    $('#kisteValue').text(form.find('#kiste').val());

                } else {
                    // Fehler beim Formular, zeige Fehlermeldungen auf der aktuellen Seite ('explants')
                    var errors = data.errors;
                    var errorHtml = '<div class="alert alert-danger" role="alert"><ul>';
                    for (var key in errors) {
                        errorHtml += '<li>' + errors[key] + '</li>';
                    }
                    errorHtml += '</ul></div>';
                    $('#alert-container').html(errorHtml);
                    // Hier können Sie weitere Fehlerbehandlungen hinzufügen
                }
            }
        });
    });
});
