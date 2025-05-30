export function fetchCpuUsage() {
    fetch('/cpu_usage')
        .then(response => response.json())
        .then(data => {
            const cpuUsage = `Использование: ${data.cpu_usage}%`;
            const cpuFrequency = `Частота: ${data.current_freq} MHz`;
            const physicalCores = `Физические ядра: ${data.physical_cores}`;
            const logicalCores = `Логические ядра: ${data.logical_cores}`;

            document.getElementById('cpu-usage').innerHTML = `
                ${cpuUsage}<br><hr>${cpuFrequency}<br>${physicalCores}<br>${logicalCores}
            `;
        })
        .catch(error => console.error('Ошибка при запросе CPU:', error));
}
