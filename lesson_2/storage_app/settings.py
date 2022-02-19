from pathlib import Path
import enum

from fastapi import Depends
from pydantic import BaseSettings

from storage import Storage
from storage.persistence import FilePersistence, Persistence
from storage.serializer import JSONSerializer, YAMLSerializer, Serializer

from lesson_2.storage_app.redis_persistence import RedisPersistence
from lesson_2.storage_app.toml_serializer import TOMLSerializer


class SerializerType(enum.Enum):
    JSON = "json"
    YAML = "yaml"
    TOML = "toml"


class PersistenceType(enum.Enum):
    FILE = "file"
    REDIS = "redis"


class Settings(BaseSettings):
    serializer: SerializerType = SerializerType.JSON
    persistence: PersistenceType = PersistenceType.FILE


def get_settings() -> Settings:
    return Settings()


def _setup_file_persistence():
    storage_dir = Path("local_storage")
    if not storage_dir.exists():
        storage_dir.mkdir()

    return FilePersistence(storage_dir)


def _setup_redis_persistence():
    return RedisPersistence("localhost", 6379)


def get_persistence(settings: Settings = Depends(get_settings)) -> Persistence:
    if settings.persistence == PersistenceType.REDIS:
        return _setup_redis_persistence()
    else:
        return _setup_file_persistence()


def get_serializer(settings: Settings = Depends(get_settings)) -> Serializer:
    if settings.serializer == SerializerType.YAML:
        return YAMLSerializer()
    elif settings.serializer == SerializerType.TOML:
        return TOMLSerializer()
    else:
        return JSONSerializer()


def get_storage(persistence: Persistence = Depends(get_persistence)) -> Storage:
    return Storage(
        serializer=YAMLSerializer(),
        persistence=persistence,
    )
