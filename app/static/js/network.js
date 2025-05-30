export function fetchNetworkInfo() {
    fetch('/network_info')
        .then(response => response.json())
        .then(data => {
            document.getElementById('sent-bytes').textContent = data.bytes.sent;
            document.getElementById('received-bytes').textContent = data.bytes.recv;
            document.getElementById('sent-packets').textContent = data.packets.sent;
            document.getElementById('received-packets').textContent = data.packets.recv;
        })
        .catch(error => console.error('Ошибка при запросе сети:', error));
}
