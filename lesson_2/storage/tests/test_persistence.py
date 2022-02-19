import pathlib

import pytest

from storage.persistence import FilePersistence


def test_file_persistence(tmpdir: pathlib.Path):
    file_persistence = FilePersistence(tmpdir)

    id_ = file_persistence.write("hello world")

    file_path = tmpdir / str(id_)
    assert file_path.exists()
    assert file_path.read_text(encoding="utf8") == "hello world"

    restored = file_persistence.read(id_)

    assert restored == "hello world"
