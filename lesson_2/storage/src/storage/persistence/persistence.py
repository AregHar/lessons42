import abc
import uuid


class Persistence(abc.ABC):
    @abc.abstractmethod
    def write(self, data) -> uuid.UUID:
        raise NotImplementedError

    @abc.abstractmethod
    def read(self, stored_id: uuid.UUID):
        raise NotImplementedError

    @staticmethod
    def _generate_id() -> uuid.UUID:
        return uuid.uuid4()
