const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
let currentTimeout = null;

const appendAlert = (message, type) => {
    // Очищаем предыдущий таймаут если он существует
    if (currentTimeout) {
        clearTimeout(currentTimeout);
    }

    // Удаляем существующий алерт если он есть
    const existingAlert = alertPlaceholder.querySelector('.alert');
    if (existingAlert) {
        existingAlert.remove();
    }

    // Создаем новый алерт
    const wrapper = document.createElement('div');
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible fade show" role="alert">`,
        `   <div>${message}</div>`,
        '</div>'
    ].join('');

    // Добавляем новый алерт
    alertPlaceholder.append(wrapper);
    alertPlaceholder.classList.add('show');

    // Устанавливаем новый таймаут
    currentTimeout = setTimeout(() => {
        const alertElement = alertPlaceholder.querySelector('.alert');
        if (alertElement) {
            alertElement.classList.remove('show');
            alertElement.addEventListener('transitionend', () => {
                alertPlaceholder.classList.remove('show');
                alertElement.remove();
            });
        }
    }, 1000);
};

const alertTrigger = document.getElementById('liveAlertBtn');
if (alertTrigger) {
    alertTrigger.addEventListener('click', () => {
        appendAlert('Товар добавлен в корзину!', 'success');
    });
}