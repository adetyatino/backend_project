import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)


def set_key(key: str, value: str, expire: int = None):
    redis_client.set(name=key, value=value, ex=expire)


def get_key(key: str):
    return redis_client.get(key)


def delete_key(key: str):
    redis_client.delete(key)
