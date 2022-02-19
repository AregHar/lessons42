import yaml

from .serializer import Serializer


class YAMLSerializer(Serializer):
    def dump(self, value) -> str:
        return yaml.dump(value)

    def load(self, value: str):
        return yaml.load(value, yaml.Loader)
