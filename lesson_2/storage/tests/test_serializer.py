import json

import pytest
import yaml

from storage.serializer import JSONSerializer
from storage.serializer import YAMLSerializer

from lesson_2.storage.tests.fixtures import sample


@pytest.fixture
def json_serializer():
    return JSONSerializer()


@pytest.fixture
def yaml_serializer():
    return YAMLSerializer()


def test_json_serializer(sample, json_serializer):
    serialized = json_serializer.dump(sample)
    assert serialized == json.dumps(sample)

    restored = json_serializer.load(serialized)
    assert restored == sample


def test_yaml_serializer(sample, yaml_serializer):
    serialized = yaml_serializer.dump(sample)
    assert serialized == yaml.dump(sample)

    restored = yaml_serializer.load(serialized)
    assert restored == sample
