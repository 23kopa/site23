import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=0,
    password='user23redis',
    decode_responses=True
)
