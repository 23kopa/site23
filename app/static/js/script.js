  // Вызов функции при загрузке страницы
  window.onload = function() {
    fetchCpuUsage(); // Запросим данные о CPU
    fetchNginxStatus(); // Запросим данные о CPU
    fetchNetworkInfo();
  };

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

  function fetchNginxStatus() {
    fetch('/nginx_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('nginx-status').textContent = data.status;
        });
        
}

function fetchSslStatus() {
    fetch('/ssl_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ssl-status').textContent = data.status;
        });
}

  // Функция для запроса информации о CPU
// Функция для запроса информации о CPU
function fetchCpuUsage() {
    fetch('/cpu_usage')
      .then(response => response.json())
      .then(data => {
        // Обновить элементы на странице с информацией о CPU
        const cpuUsage = `Использование: ${data.cpu_usage}%`;
        const cpuFrequency = `Частота: ${data.current_freq} MHz`;
        const physicalCores = `Физические ядра: ${data.physical_cores}`;
        const logicalCores = `Логические ядра: ${data.logical_cores}`;
        
        // Обновить вывод на страницу с разрывами строк для каждого параметра
        document.getElementById('cpu-usage').innerHTML = `
          ${cpuUsage}<br>
          <hr>
          ${cpuFrequency}<br>
          ${physicalCores}<br>
          ${logicalCores}
        `;
      })
      .catch(error => {
        console.error('Ошибка при запросе информации о CPU:', error);
      });
}

function fetchNetworkInfo() {
    fetch('/network_info')
        .then(response => response.json())
        .then(data => {
            // Отображение байтов
            document.getElementById('sent-bytes').textContent = data.bytes.sent;
            document.getElementById('received-bytes').textContent = data.bytes.recv;

            // Отображение пакетов
            document.getElementById('sent-packets').textContent = data.packets.sent;
            document.getElementById('received-packets').textContent = data.packets.recv;
        })
        .catch(error => {
            console.error('Ошибка при запросе информации о сети:', error);
        });
}

// Добавляем обработчик событий на каждую строку таблицы
document.querySelectorAll('.table tr').forEach(row => {
  row.addEventListener('click', function() {
      // Находим ячейку <td> во второй колонке (адрес)
      const cell = this.cells[1];  // Индекс 1 - вторая ячейка (адрес)
      
      // Создаем временный элемент input для копирования текста
      const tempInput = document.createElement('input');
      tempInput.value = cell.textContent;  // Устанавливаем значение в input
      document.body.appendChild(tempInput);
      
      // Выбираем и копируем текст в input
      tempInput.select();
      document.execCommand('copy');
      
      // Удаляем временный input
      document.body.removeChild(tempInput);

      // Показать кастомное уведомление
      const notification = document.getElementById('copyNotification');
      notification.style.display = 'block';

      // Скрыть уведомление через 2 секунды
      setTimeout(() => {
          notification.style.display = 'none';
      }, 2000);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  if (document.body.classList.contains("auth-page")) {
    const c = document.getElementById("matrix");
    if (!c) return;

    const ctx = c.getContext("2d");
    c.height = window.innerHeight;
    c.width = window.innerWidth;

    const letters = "アァイィウエカキクケコサシスセソ0123456789";
    const fontSize = 18;
    const columns = c.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
      ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
      ctx.fillRect(0, 0, c.width, c.height);

      ctx.fillStyle = "rgba(0, 255, 0, 0.1)";
      ctx.font = `${fontSize}px monospace`;

      for (let i = 0; i < drops.length; i++) {
        const text = letters[Math.floor(Math.random() * letters.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > c.height && Math.random() > 0.995) drops[i] = 0;
        drops[i]++;
      }
      setTimeout(() => requestAnimationFrame(draw), 50); // 50мс между кадрами = 20 FPS
    }

    draw();

    // адаптация под ресайз окна
    window.addEventListener("resize", () => {
      c.width = window.innerWidth;
      c.height = window.innerHeight;
    });
  }
});


