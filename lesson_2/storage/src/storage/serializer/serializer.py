import abc


class Serializer(abc.ABC):
    @abc.abstractmethod
    def dump(self, value) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def load(self, value: str):
        raise NotImplementedError
