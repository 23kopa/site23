""" import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_cores():
    return psutil.cpu_count(logical=False), psutil.cpu_count(logical=True)

def get_cpu_frequency():
    freq = psutil.cpu_freq()
    return freq.current, freq.min, freq.max

# Функция для получения информации о сети
def get_network_info():
    net_io = psutil.net_io_counters()  # Получаем статистику по трафику
    net_if_addrs = psutil.net_if_addrs()  # Получаем информацию об интерфейсах

    network_info = {
        'bytes': {
            'sent': net_io.bytes_sent,  # Отправлено байтов
            'recv': net_io.bytes_recv,  # Получено байтов
        },
        'packets': {
            'sent': net_io.packets_sent,  # Отправлено пакетов
            'recv': net_io.packets_recv,  # Получено пакетов
        },
    }
    return network_info """