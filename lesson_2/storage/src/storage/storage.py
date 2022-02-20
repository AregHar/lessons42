import uuid

from storage.persistence import Persistence
from storage.serializer import Serializer


# facade design pattern, encapsulate low level functionality, provide high-level easy-to-use interface
class Storage:
    """
    Storage stores dicts in persistent memory.
    """

    # dependency inversion, depend on abstract classes
    def __init__(self, persistence: Persistence, serializer: Serializer):
        # composition
        self._persistence = persistence
        self._serializer = serializer

    # utility method, does it fit here?
    def generate_key(self, obj: dict) -> str:
        return str(uuid.uuid4())

    # delegate writing to the composed objects, using their public methods
    def write(self, key: str, obj: dict) -> None:
        self._persistence.write(key, self._serializer.dump(obj))

    def read(self, key: str) -> dict:
        return self._serializer.load(self._persistence.read(key))
