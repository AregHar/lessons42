import redis

from storage.persistence import Persistence


class RedisPersistence(Persistence):
    def __init__(self, host: str, port: int):
        self._redis = redis.Redis(host=host, port=port, db=0)

    def write(self, key: str, data: str) -> None:
        self._redis.set(key, data)

    def read(self, key: str) -> str:
        return self._redis.get(key)
