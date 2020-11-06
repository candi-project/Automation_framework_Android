import unittest
import pytest
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from appium import webdriver
from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
import time

from AppiumFrameWork.pages.LoginPage import LoginPage
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("beforeClass", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInAdmin(self):
        self.gt.enterAdmin()
        self.gt.clickOnSubmit()

    @pytest.mark.run(order=4)
    def test_openloginpage(self):

        self.bp.keyCode(4)

        wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        wait.until(lambda x: x.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("LOGIN"))')).click()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginBtn()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("App Launched.")

        self.gt.scrollAndClick()

        # wait = WebDriverWait(self.driver, 20, poll_frequency=1,
        #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
        #                                          NoSuchElementException])
        # wait.until(lambda x: x.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("LOGIN"))')).click()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLoginBtn()
        self.gt.verifyAdminScreen()



















