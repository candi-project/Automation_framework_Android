import unittest
import pytest

from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
import time

from AppiumFrameWork.pages.ContactUsFormPage import ContactForm


@pytest.mark.usefixtures("beforeClass", "setUp")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched.")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()



















# driver1 = Driver()
# log =cl.customLogger()
#
# driver = driver1.getDriverMethod()
# cf = ContactForm(driver)

# cf.clickContactFormButton()
# cf.verifyContactPage()
# cf.enterName()
# cf.enterEmail()
# cf.enterAddress()
# cf.enterMNumber()
# cf.clickSubmitButton()

#bp = BasePage(driver)

#log.info("Launch App.")
# element = bp.waitForElement('de.proglove.connect:id/connectionButton', "id")
# element.click()

# SCAN2PAIR = bp.isDisplayed('de.proglove.connect:id/connectionButton', "id")
# print(SCAN2PAIR)
# bp.clickElement('de.proglove.connect:id/connectionButton', "id")
# time.sleep(3)
# bp.screenShot("permission")

