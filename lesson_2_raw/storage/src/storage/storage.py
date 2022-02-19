import uuid
import json
import pathlib


class Storage:
    def __init__(self, storage_dir: pathlib.Path):
        self._storage_dir = storage_dir

    def generate_key(self, obj: dict) -> str:
        return str(uuid.uuid4())

    def write(self, key: str, obj: dict) -> None:
        file_path = self._create_file_path(key)
        with open(file_path, encoding='utf8', mode='w') as f:  # persistence
            f.write(json.dumps(obj))  # presentation

    def read(self, key: str) -> dict:
        file_path = self._create_file_path(key)
        with open(file_path, encoding='utf8') as f:
            return json.load(f)

    def _create_file_path(self, key: str) -> pathlib.Path:
        return self._storage_dir / key
