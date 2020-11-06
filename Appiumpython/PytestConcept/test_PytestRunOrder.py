import pytest

@pytest.mark.run(order=4)
def test_methodA():
    print("You are awesome.")

@pytest.mark.run(order=3)
def test_methodB():
    print("Automation rocks!")

@pytest.mark.run(order=1)
def test_methodC():
    print("Automation C!")

@pytest.mark.run(order=2)
def test_methodD():
    print("Automation D!")