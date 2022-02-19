import json

from .serializer import Serializer


class JSONSerializer(Serializer):
    def dump(self, value) -> str:
        return json.dumps(value)

    def load(self, value: str):
        return json.loads(value)
