import pytest

from storage import Storage

from lesson_2.storage.tests.test_serializer import json_serializer
from lesson_2.storage.tests.test_persistence import file_persistence


@pytest.fixture
def sample():
    return {"lesson": 2, "subject": "SOLID"}


@pytest.fixture
def json_file_storage(json_serializer, file_persistence):
    return Storage(
        persistence=file_persistence,
        serializer=json_serializer,
    )


def test_json_storage(sample, json_file_storage):
    key = json_file_storage.generate_key(sample)
    json_file_storage.write(key, sample)
    sample_restored = json_file_storage.read(key)

    assert sample_restored == sample
