document.addEventListener('DOMContentLoaded', function () {
    // Пример уведомления при запуске бота
    const startButton = document.querySelector('a[href="/start_bot"]');
    if (startButton) {
        startButton.addEventListener('click', function() {
            toastr.success('Бот успешно запущен!', 'Успех');
        });
    }

    // Пример уведомления при остановке бота
    const stopButton = document.querySelector('a[href="/stop_bot"]');
    if (stopButton) {
        stopButton.addEventListener('click', function() {
            toastr.error('Бот был остановлен.', 'Ошибка');
        });
    }

    // Пример уведомления при перезапуске бота
    const restartButton = document.querySelector('a[href="/restart_bot"]');
    if (restartButton) {
        restartButton.addEventListener('click', function() {
            toastr.info('Перезапуск бота...', 'Информация');
        });
    }
});

// Функция для запроса данных о диске
function fetchDiskUsage() {
    fetch('/get_disk_usage')
        .then(response => response.json())  // Получаем данные в формате JSON
        .then(data => {
            // Формируем HTML для отображения данных
            let content = '<ul>';
            data.forEach(item => {
                content += `<li><strong>Директория:</strong> ${item.directory} - <strong>Размер:</strong> ${item.size}</li>`;
            });
            content += '</ul>';
            
            // Вставляем данные в тело модального окна
            document.getElementById('diskUsageContent').innerHTML = content;
        })
        .catch(error => {
            console.error('Ошибка при получении данных:', error);
            document.getElementById('diskUsageContent').innerHTML = 'Произошла ошибка при получении данных.';
        });
}

// Другие скрипты здесь
document.addEventListener("DOMContentLoaded", function () {
    // Ваши другие события
});
