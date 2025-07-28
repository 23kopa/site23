document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.modal-form').forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const cardId = form.id.replace('form-', '');
            const resultDiv = document.getElementById(`result-${cardId}`);

            try {
                const response = await fetch(form.getAttribute('action') || window.location.pathname, {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'X-CSRFToken': formData.get('csrf_token'),
                    },
                    body: formData
                });

                if (!response.ok) {
                    throw new Error(`Ошибка: ${response.status}`);
                }

                const data = await response.json();

                if (data.url) {
                    // Закрыть текущий модал (создание токена)
                    const createModal = bootstrap.Modal.getInstance(document.getElementById(`modal-${cardId}`));
                    if (createModal) createModal.hide();

                    // Показать новый модал с результатом
                    const resultModalEl = document.getElementById(`modal-result-${cardId}`);
                    const resultModal = new bootstrap.Modal(resultModalEl);
                    
                    // Установить ссылку
                    const linkElem = document.getElementById(`token-link-${cardId}`);
                    linkElem.href = data.url;
                    linkElem.textContent = data.url;

                    // Очистить поле информации
                    const infoDiv = document.getElementById(`token-info-${cardId}`);
                    infoDiv.textContent = '';

                    // Показать модал
                    resultModal.show();

                    // Обработчик кнопки менеджмента токена
                    const manageBtn = document.getElementById(`manage-btn-${cardId}`);
                    manageBtn.onclick = async () => {
                        // Сделать запрос к вашему API, чтобы получить информацию о триггере токена
                        // Предполагаем, что есть эндпоинт, например: /api/token_info/<token_uid>

                        // Извлечь token_uid из URL
                        const tokenUid = data.url.split('/').pop();

                        try {
                            const infoResponse = await fetch(`/api/token_info/${tokenUid}`, {
                                credentials: 'include',
                            });
                            if (!infoResponse.ok) throw new Error(`Ошибка: ${infoResponse.status}`);

                            const infoData = await infoResponse.json();

                            // Вывести инфо в infoDiv (можно настроить формат вывода)
                            infoDiv.innerHTML = `<pre>${JSON.stringify(infoData, null, 2)}</pre>`;
                        } catch (err) {
                            infoDiv.innerHTML = `<div class="alert alert-danger">Ошибка при получении информации: ${err.message}</div>`;
                        }
                    };
                } else if (data.error) {
                    resultDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
                } else {
                    resultDiv.innerHTML = `<div class="alert alert-warning">Неизвестный ответ от сервера</div>`;
                }
            } catch (err) {
                resultDiv.innerHTML = `<div class="alert alert-danger">Ошибка запроса: ${err.message}</div>`;
            }
        });
    });
});
