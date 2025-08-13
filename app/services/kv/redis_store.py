import json
import logging
from app.extensions.redis import r  # импорт клиента
from redis.exceptions import RedisError

logger = logging.getLogger(__name__)

PREFIX = "web_token:"

def store_token(token_uid: str, token_data: dict) -> None:
    key = f"{PREFIX}{token_uid}"
    try:
        r.set(key, json.dumps(token_data))
    except RedisError as e:
        logger.error(f"Redis error on store_token for {key}: {e}")
        raise

def get_token(token_uid: str) -> dict | None:
    key = f"{PREFIX}{token_uid}"
    try:
        raw = r.get(key)
        logger.info(f"get_token called with key={key}, raw={raw}")
        if raw:
            return json.loads(raw)
        return None
    except RedisError as e:
        logger.error(f"Redis error on get_token for {key}: {e}")
        return None

def update_token(token_uid: str, updates: dict) -> None:
    key = f"{PREFIX}{token_uid}"
    try:
        raw = r.get(key)
        if raw:
            data = json.loads(raw)
            data.update(updates)
            r.set(key, json.dumps(data))
    except RedisError as e:
        logger.error(f"Redis error on update_token for {key}: {e}")
        raise
