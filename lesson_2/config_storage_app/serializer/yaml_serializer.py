import yaml

from storage.serializer import Serializer


class YamlSerializer(Serializer):
    def dump(self, obj: dict) -> str:
        return yaml.dump(obj)

    def load(self, obj: str) -> dict:
        return yaml.load(obj, yaml.Loader)
