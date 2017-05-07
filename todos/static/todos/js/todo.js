window.addEventListener('load', handleLoad);

function handleLoad() {
    var form = document.querySelector('.todo-form form');
    var messages = document.querySelector('.messages');

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }

    if (messages) {
        console.log('Message will be hidden after 5 seconds.');
        setTimeout(hideMessages, 5000);
    }
}

function hideMessages() {
    var messages = document.querySelector('.messages');

    messages.style.display = 'none';
}

function handleFormSubmit(e) {
    // Frontend Validation here.
    var titleInput = document.querySelector('#input-todo-title');
    var title = titleInput.value.trim();

    if (!title || title === '') {
        alert('Please enter the title.');
        titleInput.focus();
        e.preventDefault();
    }
}
