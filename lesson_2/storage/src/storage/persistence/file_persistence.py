import pathlib

from .persistence import Persistence


# open/closed
# Liskov principle, implements the Persistence interface
class FilePersistence(Persistence):
    # initialization is implementation specific
    def __init__(self, storage_dir: pathlib.Path):
        self._storage_dir = storage_dir

    def write(self, key: str, data: str) -> None:
        file_path = self._create_file_path(key)
        with open(file_path, encoding="utf8", mode="w") as f:
            f.write(data)

    def read(self, key: str) -> str:
        file_path = self._create_file_path(key)
        with open(file_path, encoding="utf8") as f:
            return f.read()

    # implementation specific thus private. No client code should rely on it.
    def _create_file_path(self, key: str) -> pathlib.Path:
        return self._storage_dir / key
