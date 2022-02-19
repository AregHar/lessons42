from pathlib import Path
import uuid

from .persistence import Persistence


class FilePersistence(Persistence):
    def __init__(self, storage_dir: Path):
        self._storage_dir = storage_dir

    def _make_file_path(self, stored_id) -> Path:
        return self._storage_dir / str(stored_id)

    def write(self, data: str) -> uuid.UUID:
        stored_id = self._generate_id()
        with open(self._make_file_path(stored_id), encoding="utf8", mode="w") as f:
            f.write(data)
        return stored_id

    def read(self, stored_id: uuid.UUID):
        with open(self._make_file_path(stored_id), encoding="utf8") as f:
            return f.read()
