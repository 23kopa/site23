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

document.addEventListener("DOMContentLoaded", function () {
    const terminalOutput = document.getElementById('terminal-output');
    const textContainer = document.querySelector('.text');
    const cursor = document.querySelector('.cursor');

    const text = ">>> Добро пожаловать, бро! Тут без багов, только фичи <3";

    let i = 0;
    const typingSpeed = 100; // скорость печати (мс)

    // Функция для печати текста
    function typeText() {
        if (i < text.length) {
            textContainer.textContent += text.charAt(i); // добавляем символ в текст
            i++;
            setTimeout(typeText, typingSpeed);
        } else {
            // Когда текст полностью выведен, курсор мигает
            cursor.style.animation = 'blink 0.7s step-start infinite';
        }
    }

    // Запуск анимации текста
    typeText();
});


document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function (e) {
      const ripple = document.createElement('span');
      ripple.style.position = 'absolute';
      ripple.style.borderRadius = '50%';
      ripple.style.background = '#00ff88';
      ripple.style.opacity = '0.6';
      ripple.style.pointerEvents = 'none';
      ripple.style.width = ripple.style.height = '100px';
      ripple.style.transform = 'scale(0)';
      ripple.style.animation = 'ripple 0.6s linear';
  
      const rect = this.getBoundingClientRect();
      ripple.style.left = `${e.clientX - rect.left - 50}px`;
      ripple.style.top = `${e.clientY - rect.top - 50}px`;
  
      this.appendChild(ripple);
  
      ripple.addEventListener('animationend', () => {
        ripple.remove();
      });
    });
  });

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

