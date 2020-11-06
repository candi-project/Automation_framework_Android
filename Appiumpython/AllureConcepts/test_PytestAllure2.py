import pytest
import allure


def test_methodA():
    allureLogs("methodA-step1")
    allureLogs("methodA-step2")
    allureLogs("methodA-step3")
    allureLogs("methodA-step4")
    allureLogs("methodA-step5")
    print("You are awesome.")


def test_methodB():
    print("Automation rocks!")

@pytest.mark.skip
def test_methodC():
    print("Automation C!")


def test_methodD():
    print("Automation D!")
    assert False


def allureLogs(text):
    with allure.step(text):
        pass