import json

from .serializer import Serializer


# open/closed
# Liskov principle, implements the Persistence interface
class JsonSerializer(Serializer):
    def dump(self, obj: dict) -> str:
        return json.dumps(obj)

    def load(self, obj: str) -> dict:
        return json.loads(obj)
