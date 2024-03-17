document.addEventListener('DOMContentLoaded', function () {
    var addButton = document.getElementById('show-examples-form');
    var examplesForm = document.getElementById('add-examples-form');

    addButton.addEventListener('click', function () {
        examplesForm.style.display = examplesForm.style.display === 'none' ? 'block' : 'none';
    });
});
