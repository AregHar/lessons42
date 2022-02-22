from pathlib import Path
import enum

from pydantic import BaseSettings
from fastapi import Depends

from storage import Storage
from storage.serializer import JsonSerializer, Serializer
from storage.persistence import FilePersistence, Persistence

from lesson_2.config_storage_app.serializer.yaml_serializer import YamlSerializer
from lesson_2.config_storage_app.serializer.toml_serializer import TomlSerializer
from lesson_2.config_storage_app.persistence.redis_persistence import RedisPersistence
from lesson_2.config_storage_app.persistence.sqlite_persistence import SQLitePersistence


# restrict serializer types down to the accepted values. Better than simple str
class SerializerType(enum.Enum):
    JSON = "json"
    YAML = "yaml"
    TOML = "toml"


# restrict persistence types down to the accepted values. Better than simple str
class PersistenceType(enum.Enum):
    FILE = "file"
    REDIS = "redis"
    SQLITE = "sqlite"


# Settings gathers environment variables, loading them in one place.
class Settings(BaseSettings):
    serializer: SerializerType  # env var will be checked against the enum values
    persistence: PersistenceType  # env var will be checked against the enum values


settings = Settings()


# resolves the persistence dependency
def get_persistence() -> Persistence:
    if settings.persistence == PersistenceType.REDIS:
        return RedisPersistence("localhost", 6379)
    elif settings.persistence == PersistenceType.FILE:
        storage_dir = Path("local-storage")
        if not storage_dir.exists():
            storage_dir.mkdir()
        return FilePersistence(storage_dir)
    elif settings.persistence == PersistenceType.SQLITE:
        return SQLitePersistence()


# resolves the serializer dependency
def get_serializer() -> Serializer:
    if settings.serializer == SerializerType.YAML:
        return YamlSerializer()
    elif settings.serializer == SerializerType.JSON:
        return JsonSerializer()
    elif settings.serializer == SerializerType.TOML:
        return TomlSerializer()


# resolves the storage dependency
def get_storage(
    persistence: Persistence = Depends(get_persistence),
    serializer: Serializer = Depends(get_serializer),
) -> Storage:
    # dynamically assemble the storage instance with desired configuration.
    # We use composition here
    return Storage(
        persistence=persistence,
        serializer=serializer,
    )
