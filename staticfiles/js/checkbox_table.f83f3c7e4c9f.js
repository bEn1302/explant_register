document.getElementById('selectAll').addEventListener('change', handleSelectAll);

function handleSelectAll() {
    const tableElement = document.querySelector('#explant-table');
    if (!tableElement) {
        console.error('Table element not found');
        return;
    }

    const className = tableElement.classList.contains('huefte') ? 'huefte-row-checkbox' : 'knie-row-checkbox';
    const checkboxes = document.querySelectorAll('.' + className);
    checkboxes.forEach((checkbox) => {
        checkbox.checked = this.checked;
    });
}