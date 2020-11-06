import pytest

@pytest.yield_fixture(scope="module")
def beforeClass():
    print("Before class.")
    yield
    print("After class.")

@pytest.yield_fixture()
def setUp():
    print("This is a setup guide.")
    yield
    print("After method.")