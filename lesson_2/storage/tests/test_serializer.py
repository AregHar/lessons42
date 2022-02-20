import pytest

from storage.serializer import Serializer
from storage.serializer import JsonSerializer


@pytest.fixture
def sample():
    return {"lesson": 2, "subject": "SOLID"}


@pytest.fixture()
def json_serializer():
    return JsonSerializer()


def test_json_serializer(sample, json_serializer: Serializer):
    dumped_sample = json_serializer.dump(sample)
    assert dumped_sample == '{"lesson": 2, "subject": "SOLID"}'

    loaded_sample = json_serializer.load(dumped_sample)
    assert loaded_sample == sample
