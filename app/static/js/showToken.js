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
                    
                    const displayContainer = document.getElementById(`token-display-${cardId}`);
                    displayContainer.innerHTML = '';  // очистка перед вставкой

                    if (data.token_type === 'qr') {
                        // Показать QR-код
                        const img = document.createElement('img');
                        img.src = data.qr_image_url;
                        img.alt = 'QR код';
                        img.className = 'img-fluid';  // адаптивное изображение
                        displayContainer.appendChild(img);
                    } else {
                        // Показать ссылку (webbug и др.)
                        displayContainer.innerHTML = `
                            <p>Ссылка на токен:</p>
                            <div class="d-flex align-items-center mb-3 px-3 py-2 border rounded"
                                style="max-width: 100%; overflow-x: auto; background-color: white;">
                                <span id="token-link-${cardId}" class="me-2 text-truncate"
                                    style="cursor: pointer; user-select: all; min-width: 0; flex-grow: 1; background-color: white;"
                                    onclick="copyTokenLink('${cardId}')">
                                    ${data.url}
                                </span>
                                <i class="fa fa-clipboard" style="cursor: pointer; flex-shrink: 0;"
                                    onclick="copyTokenLink('${cardId}')" title="Скопировать"></i>
                            </div>
                        `;
                    }

                    // Очистить поле информации
                    const infoDiv = document.getElementById(`token-info-${cardId}`);
                    infoDiv.textContent = '';

                    resultModal.show();

                    // Обработчик кнопки менеджмента токена
                    const manageBtn = document.getElementById(`manage-btn-${cardId}`);
                    manageBtn.onclick = async () => {
                        const tokenUid = data.url.split('/').slice(-2, -1)[0];

                        try {
                            const infoResponse = await fetch(`/token/api/token_info/${tokenUid}`, {
                                credentials: 'include',
                            });
                            if (!infoResponse.ok) throw new Error(`Ошибка: ${infoResponse.status}`);

                            const infoData = await infoResponse.json();

                            infoDiv.innerHTML = formatTokenInfoAsTable(infoData);
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

function formatTokenInfoAsTable(data) {
    const geo = data.token_metadata?.geo_info || {};
    const userAgent = data.token_metadata?.user_agent || '';
    const ip = data.token_metadata?.ip || '';
    const time = data.token_metadata?.trigger_time || '';
    const url = data.token_metadata?.trigger_url || '';

    return `
        <div style="max-width: 100%;">
            <table class="table table-bordered table-sm token-info-table w-100">
                <tr><th>UID токена</th><td>${data.token_uid}</td></tr>
                <tr><th>Сообщение оповещения</th><td>${data.alert_message || '-'}</td></tr>
                <tr><th>Email</th><td>${data.email || '-'}</td></tr>
                <tr><th>Время срабатывания</th><td>${time || '-'}</td></tr>
                <tr><th>IP адрес</th><td>${ip}</td></tr>
                <tr><th>User-Agent</th><td>${userAgent}</td></tr>
                <tr><th>Город</th><td>${geo.city || '-'}</td></tr>
                <tr><th>Регион</th><td>${geo.regionName || '-'}</td></tr>
                <tr><th>Страна</th><td>${geo.country || '-'}</td></tr>
                <tr><th>Провайдер</th><td>${geo.isp || '-'}</td></tr>
                <tr><th>Организация</th><td>${geo.org || '-'}</td></tr>
                <tr><th>AS</th><td>${geo.as || '-'}</td></tr>
                <tr><th>Координаты</th><td>${geo.lat || '-'}, ${geo.lon || '-'}</td></tr>
                <tr><th>ZIP</th><td>${geo.zip || '-'}</td></tr>
                <tr><th>URL вызова</th><td><a href="${url}" target="_blank">${url}</a></td></tr>
            </table>
        </div>
    `;
}

function copyTokenLink(cardId) {
    const el = document.getElementById('token-link-' + cardId);
    const range = document.createRange();
    range.selectNodeContents(el);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    try {
        document.execCommand('copy');
        sel.removeAllRanges();
    } catch (err) {
        console.error('Ошибка копирования', err);
    }
}
