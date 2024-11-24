const form = document.querySelector('form'); // Находим форму на странице
const resultDiv = document.getElementById('liveAlertPlaceholder'); // Находим элемент для вывода результата

form.addEventListener('submit', (event) => {
    event.preventDefault(); // Предотвращаем стандартное поведение формы (перезагрузку страницы)

    const formData = new FormData(form); // Создаем объект FormData с данными из формы

    // Отправляем AJAX-запрос
    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.json()) // Получаем ответ от сервера в формате JSON
    .then(data => {
        // Обрабатываем ответ сервера
        if (data.status === 'success') {
            // Если товар успешно добавлен в корзину, выводим сообщение об успехе
            resultDiv.innerHTML = '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                'Товар добавлен в корзину!' +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
        } else {
            // Если произошла ошибка, выводим сообщение об ошибке
            resultDiv.innerHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">' +
                'Ошибка: ' + data.message +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
        }
    })
    .catch(error => {
        console.error('Ошибка:', error); // Выводим ошибку в консоль
    });
});