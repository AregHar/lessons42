import abc


# single responsibility
# small focused interface
class Serializer(abc.ABC):
    @abc.abstractmethod
    def dump(self, obj: dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def load(self, obj: str) -> dict:
        raise NotImplementedError
