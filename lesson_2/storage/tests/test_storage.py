from storage import Storage
from storage.persistence import FilePersistence
from storage.serializer import JSONSerializer, YAMLSerializer

from lesson_2.storage.tests.fixtures import sample


def test_storage(sample, tmpdir):
    storage = Storage(
        serializer=JSONSerializer(),
        persistence=FilePersistence(tmpdir),
    )

    id_ = storage.store(sample)
    restored = storage.restore(id_)

    assert restored == sample
