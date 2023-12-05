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
    // Füge weitere Felder hinzu...

    // Überwache Änderungen und speichere sie lokal
    $('#id_ursache').on('input', function () {
        localStorage.setItem('ursache', $(this).val());
    });
    $('#id_verfuegbarkeit').on('change', function () {
        localStorage.setItem('verfuegbarkeit', $(this).prop('checked'));
    });
    $('#id_herkunftsort').on('input', function () {
        localStorage.setItem('herkunftsort', $(this).val());
    });
    $('#id_entnahme_datum').on('input', function () {
        localStorage.setItem('entnahme_datum', $(this).val());
    });
    $('#id_eingang_datum').on('input', function () {
        localStorage.setItem('eingang_datum', $(this).val());
    });
    $('#id_bruchgeschehen').on('input', function () {
        localStorage.setItem('bruchgeschehen', $(this).val());
    });
    $('#id_nutzungsdauer').on('input', function () {
        localStorage.setItem('nutzungsdauer', $(this).val());
    });
    $('#id_reinigung').on('change', function () {
        localStorage.setItem('reinigung', $(this).prop('checked'));
    });
});