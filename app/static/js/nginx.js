export function fetchNginxStatus() {
    fetch('/nginx_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('nginx-status').textContent = data.status;
        });
}

export function fetchSslStatus() {
    fetch('/ssl_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ssl-status').textContent = data.status;
        });
}
