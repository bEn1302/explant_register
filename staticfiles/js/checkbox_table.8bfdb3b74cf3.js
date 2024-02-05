document.getElementById('selectAll').addEventListener('change', function() {
    var isHuefteTab = document.querySelector('#explant-table').classList.contains('huefte');
    var checkboxClass = isHuefteTab ? '.huefte-row-checkbox' : '.knie-row-checkbox';
    var checkboxes = document.querySelectorAll(checkboxClass);
    
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = this.checked;
    }
});
