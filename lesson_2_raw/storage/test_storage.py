import pytest

from storage import Storage


@pytest.fixture
def sample():
    return {
        "lesson": 2,
        "subject": "SOLID"
    }


def test_storage(sample, tmpdir):
    storage = Storage(tmpdir)
    key: str = storage.generate_key(sample)
    storage.write(key, sample)
    sample_restored = storage.read(key)

    assert sample_restored == sample
