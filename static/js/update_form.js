// $(document).ready(function () {
//     // AJAX-Anfrage beim Absenden des Formulars im Modal
//     $('#update-form').submit(function (e) {
//         e.preventDefault(); // Verhindert das Standardverhalten des Formulars

//         var form = $(this);

//         $.ajax({
//             type: 'POST',
//             url: form.attr('action'), // Verwenden Sie den action-Wert aus dem Formular
//             data: form.serialize(),
//             success: function (data) {
//                 if (data.success) {
//                     // Erfolgreiche Aktualisierung, zeige Erfolgsmeldung im Modal
//                     $('#alert-container').html('<div class="alert alert-success" role="alert">Lagerort erfolgreich aktualisiert.</div>');
//                 } else {
//                     // Fehler beim Formular, zeige Fehlermeldung im Modal
//                     $('#alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Aktualisieren des Lagerorts.</div>');
//                 }
//             }
//         });
//     });
// });
$(document).ready(function() {
    $('#update-form').on('submit', function(event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $('#patientModal').modal('show');
                    $('#alert-container').html('<div class="alert alert-success" role="alert">Lagerort erfolgreich aktualisiert.</div>');

                    // Seite neu laden, um die aktualisierten Daten anzuzeigen
                    window.location.reload();
                } else {
                    $('#alert-container').html('<div class="alert alert-danger" role="alert">Fehler beim Aktualisieren des Lagerorts.</div>' + response.errors);
                }
            },
            error: function() {
                // Fehlerbehandlung
            }
        });
    });
});
