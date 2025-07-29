import redis

r = redis.Redis(
    host='172.26.2.84', # IP-адрес WSL-инстанса
    port=6379,
    db=0,
    decode_responses=True
)
