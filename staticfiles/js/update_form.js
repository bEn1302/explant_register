$(document).ready(function() {
    $('#update-form{{ explant.id }}').submit(function(e) {
        e.preventDefault();

        var form = $(this);

        // Fügen Sie ein verstecktes Eingabefeld für die Checkbox ein, falls sie nicht aktiviert ist
        if (!form.find('input[name="recycelt"]').is(':checked')) {
            form.append('<input type="hidden" name="recycelt" value="false">');
        }

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form.serialize(),
            success: function(data) {
                if (data.success) {
                    $('#alert-container').html('<div class="alert alert-success" role="alert">Lagerort erfolgreich aktualisiert.</div>');
                } else {
                    $('#alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Aktualisieren des Lagerorts.</div>');
                }
            },
            error: function() {
                $('#alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Senden der Anfrage.</div>');
            }
        });
    });
});