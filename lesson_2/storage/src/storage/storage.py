import uuid

from lesson_2.storage.src.storage.serializer import Serializer
from lesson_2.storage.src.storage.persistence import Persistence


class Storage:
    def __init__(self, serializer: Serializer, persistence: Persistence):
        # SRP
        self._serializer = serializer  # presentation, local_storage format
        self._persistence = persistence  # persistence layer

    def store(self, data) -> uuid.UUID:
        return self._persistence.write(self._serializer.dump(data))

    def restore(self, stored_id: uuid.UUID):
        return self._serializer.load(self._persistence.read(stored_id))
