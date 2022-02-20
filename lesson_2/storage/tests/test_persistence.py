import pytest

from storage.persistence import Persistence
from storage.persistence import FilePersistence


@pytest.fixture()
def file_persistence(tmpdir):
    return FilePersistence(tmpdir)


def test_file_persistence(file_persistence: Persistence, tmpdir):
    key = "test_key"

    file_persistence.write(key, "hello world")

    expected_file_path = tmpdir / key
    assert expected_file_path.exists()  # check file is written

    restored_data = file_persistence.read(key)
    assert restored_data == "hello world"  # check data is restored
