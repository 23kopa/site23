/* import { fetchCpuUsage } from './cpu.js';
import { fetchDiskUsage } from './disk.js';
import { fetchNginxStatus, fetchSslStatus } from './nginx.js';
import { fetchNetworkInfo } from './network.js';
import { initMatrixEffect } from './matrix.js'; */

window.onload = function () {
    fetchCpuUsage();
    fetchNginxStatus();
    fetchNetworkInfo();
};

document.addEventListener("DOMContentLoaded", () => {
    if (document.body.classList.contains("auth-page")) {
        initMatrixEffect();
    }

    document.querySelectorAll('.table tr').forEach(row => {
        row.addEventListener('click', function () {
            const cell = this.cells[1];
            const tempInput = document.createElement('input');
            tempInput.value = cell.textContent;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);

            const notification = document.getElementById('copyNotification');
            notification.style.display = 'block';
            setTimeout(() => {
                notification.style.display = 'none';
            }, 2000);
        });
    });
});
