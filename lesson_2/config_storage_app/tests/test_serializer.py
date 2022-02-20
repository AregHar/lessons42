import pytest

from storage.serializer import Serializer
from lesson_2.config_storage_app.serializer.yaml_serializer import YamlSerializer


@pytest.fixture
def sample():
    return {"lesson": 2, "subject": "SOLID"}


@pytest.fixture()
def yaml_serializer():
    return YamlSerializer()


def test_yaml_serializer(sample, yaml_serializer: Serializer):
    dumped_sample = yaml_serializer.dump(sample)
    assert dumped_sample == "lesson: 2\nsubject: SOLID\n"

    loaded_sample = yaml_serializer.load(dumped_sample)
    assert loaded_sample == sample
