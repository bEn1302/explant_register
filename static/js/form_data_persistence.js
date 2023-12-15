$(document).ready(function () {
    // Überprüfe, ob lokale Werte gespeichert sind
    if (localStorage.getItem('ursache')) {
        $('#id_ursache').val(localStorage.getItem('ursache'));
    }
    if (localStorage.getItem('verfuegbarkeit')) {
        $('#id_verfuegbarkeit').prop('checked', localStorage.getItem('verfuegbarkeit') === 'true');
    }
    if (localStorage.getItem('herkunftsort')) {
        $('#id_herkunftsort').val(localStorage.getItem('herkunftsort'));
    }
    if (localStorage.getItem('entnahme_datum')) {
        $('#id_entnahme_datum').val(localStorage.getItem('entnahme_datum'));
    }
    if (localStorage.getItem('eingang_datum')) {
        $('#id_eingang_datum').val(localStorage.getItem('eingang_datum'));
    }
    if (localStorage.getItem('bruchgeschehen')) {
        $('#id_bruchgeschehen').val(localStorage.getItem('bruchgeschehen'));
    }
    if (localStorage.getItem('nutzungsdauer')) {
        $('#id_nutzungsdauer').val(localStorage.getItem('nutzungsdauer'));
    }
    if (localStorage.getItem('reinigung')) {
        $('#id_reinigung').prop('checked', localStorage.getItem('reinigung') === 'true');
    }
    if (localStorage.getItem('lagerort')) {
        $('#id_lagerort').val(localStorage.getItem('lagerort'));
    }
    if (localStorage.getItem('patient')) {
        $('#id_patient').val(localStorage.getItem('patient'));
    }
    if (localStorage.getItem('reoperation')) {
        $('#id_reoperation').val(localStorage.getItem('reoperation'));
    }
    if (localStorage.getItem('inlay')) {
        $('#id_inlay').val(localStorage.getItem('inlay'));
    }

    // Überwache Änderungen und speichere sie lokal
    $('#id_verfuegbarkeit').on('change', function () {
        localStorage.setItem('verfuegbarkeit', $(this).prop('checked'));
    });
    $('#id_reinigung').on('change', function () {
        localStorage.setItem('reinigung', $(this).prop('checked'));
    });
    $('#id_ursache','#id_herkunftsort','#id_bruchgeschehen','#id_nutzungsdauer','#id_entnahme_datum, #id_eingang_datum, #id_lagerort, #id_patient, #id_reoperation, #id_inlay','#id_kopf, #id_femurkomponente, #id_schaft, #id_tibiaplateau, #id_pfanne, #id_patellaersatz')
        .on('input', function () {
            localStorage.setItem($(this).attr('id'), $(this).val());
        });


    $('add-explant').on('click', function (event) {
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