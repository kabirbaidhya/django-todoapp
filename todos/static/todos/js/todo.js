window.addEventListener('load', handleLoad);

function handleLoad() {
    var form = document.querySelector('.todo-form form');

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
}

function handleFormSubmit(e) {
    // Frontend Validation here.
}
