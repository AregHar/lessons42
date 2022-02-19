import pytest


@pytest.fixture
def sample() -> dict:
    return {"lesson": "two", "subject": "SOLID"}
