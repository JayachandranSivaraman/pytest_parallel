import pytest


@pytest.fixture(scope="module", autouse=True)
def do_something():
    assert 1 == 1
    print("testing is super")