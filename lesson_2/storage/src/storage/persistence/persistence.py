import abc


# single responsibility
# small focused interface
class Persistence(abc.ABC):
    @abc.abstractmethod
    def write(self, key: str, data: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def read(self, key: str) -> str:
        raise NotImplementedError
