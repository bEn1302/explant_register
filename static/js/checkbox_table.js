document.getElementById('selectAll').addEventListener('change', function() {
    var className = document.querySelector('#explant-table').classList.contains('huefte') ? 'huefte-row-checkbox' : 'knie-row-checkbox';
    var checkboxes = document.querySelectorAll('.' + className);
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = this.checked;
    }
});