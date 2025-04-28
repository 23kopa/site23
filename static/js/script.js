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
