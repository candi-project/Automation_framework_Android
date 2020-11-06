import time

import pytest
from AppiumFrameWork.base.DriverClass import Driver

@pytest.yield_fixture(scope="class")
def beforeClass(request):
    print("Before class.")
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After class.")

@pytest.yield_fixture()
def setUp():
    print("This is a setup guide.")
    yield
    print("After method.")