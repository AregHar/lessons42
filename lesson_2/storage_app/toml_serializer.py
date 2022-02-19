import toml

from storage.serializer import Serializer


class TOMLSerializer(Serializer):
    def dump(self, value) -> str:
        return toml.dumps(value)

    def load(self, value: str):
        return toml.loads(value)
