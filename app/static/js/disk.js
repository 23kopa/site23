export function fetchDiskUsage() {
    fetch('/get_disk_usage')
        .then(response => response.json())
        .then(data => {
            let content = '<ul>';
            data.forEach(item => {
                content += `<li><strong>Директория:</strong> ${item.directory} - <strong>Размер:</strong> ${item.size}</li>`;
            });
            content += '</ul>';
            document.getElementById('diskUsageContent').innerHTML = content;
        })
        .catch(error => {
            console.error('Ошибка при получении данных:', error);
            document.getElementById('diskUsageContent').innerHTML = 'Произошла ошибка.';
        });
}
