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

function isAlreadyHidden(element) {
    return (
        element.style.display === 'none'
    );
}

function disappear(selector, duration = 1000) {
    var element = document.querySelector(selector);

    if (isAlreadyHidden(element)) {
        return;
    }

    var parts = 10;
    var changeInterval = duration / parts;
    var opacity = 1.0;

    var interval = setInterval(function () {
        opacity = opacity - (1 / parts);
        element.style.opacity = opacity;

        if (opacity === 0) {
            element.style.display = 'none';
            clearInterval(interval);
        }
    }, changeInterval);
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
