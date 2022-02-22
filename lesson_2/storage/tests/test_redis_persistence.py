import pytest
import redis

from storage.persistence import Persistence
from lesson_2.config_storage_app.persistence.redis_persistence import RedisPersistence



@pytest.fixture()
def redis_persistence():
    return RedisPersistence("localhost", 6379)


def test_redis_persistence(redis_persistence: Persistence):
    key = "test_key"

    redis_persistence.write(key, "hello world")

    restored_data = redis_persistence.read(key)
    assert restored_data == "hello world"  # check data is restored
