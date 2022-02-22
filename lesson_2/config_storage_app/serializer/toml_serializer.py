import toml

from storage.serializer import Serializer


class TomlSerializer(Serializer):
    def dump(self, obj: dict) -> str:
        return toml.dumps(obj)

    def load(self, obj: str) -> dict:
        return toml.loads(obj)
