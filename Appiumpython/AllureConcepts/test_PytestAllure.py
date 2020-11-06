import pytest


def test_methodA():
    print("You are awesome.")


def test_methodB():
    print("Automation rocks!")

@pytest.mark.skip
def test_methodC():
    print("Automation C!")


def test_methodD():
    print("Automation D!")
    assert False