import os
import subprocess

from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from AppiumFrameWork.utilities.constants import *
import AppiumFrameWork.utilities.CustomLogger as cl
import time
import allure


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class(locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().index("%d")' % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % (locatorValue)))
            # element = wait.until(lambda x: x.find_element_by_android_uiautomator(
            #     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().("text("%s")" %(locatorValue)))'))

            # wait.until(lambda x: x.find_element_by_android_uiautomator(
            # 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("LOGIN"))'))

            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath("%s" % (locatorValue)))
            return element
        else:
            self.log.error("Locator value" + locatorValue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with locator Type: " + locatorType + "and with locator value: " + locatorValue)
        except:
            self.log.error(
                "Unable to find element with locator Type: " + locatorType + "and with locator value: " + locatorValue)
            self.takeScreenShot(locatorType)
            assert False

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on element found with locator Type: " + locatorType + " and with locator value: " + locatorValue)
        except:
            self.log.error(
                "Unable to click element with locator Type: " + locatorType + " and with locator value: " + locatorValue)

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element with locator Type: " + locatorType + " and with locator value: " + locatorValue + " is displayed.")
            return True
        except:
            self.log.error(
                "Element with locator Type: " + locatorType + " and with locator value: " + locatorValue + " is not displayed.")
            self.takeScreenShot(locatorType)
            return False

    def screenShot(self, screenShotName):
        filename = screenShotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + " .png"
        screenShotDirectory = "../screenshots/"
        screenShotPath = screenShotDirectory + filename

        try:
            self.driver.save_screenshot(screenShotPath)
            self.log.info("Screenshot saved to :" + screenShotPath)
        except:
            self.log.error("Unable to save screenshot to :" + screenShotPath)

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on element found with locator Type: " + locatorType + " and with locator value: " + locatorValue)
        except:
            self.log.error(
                "Unable to send text on element with locator Type: " + locatorType + " and with locator value: " + locatorValue)
            self.takeScreenShot(locatorType)
            assert False

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
        self.log.info("ScreenShot is attached to Allure report.")

    def keyCode(self, value):
        self.driver.press_keycode(value)
        self.log.info("Pressed key code.")

    def scrollElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=None)
            element = wait.until(lambda x: x.find_element_by_android_uiautomator
            ('new UiScrollable(new UiSelector()).scrollIntoView(%s("%s"))' % (locatorType,
                                                                              locatorValue)))
            element.click()

        except:
            self.log.error("Unable to scroll")

    def push_local_file_to_the_pgconnect_directory_on_the_device_under_test(self, source_path,
                                                                            file_name_on_destination):
        """
        Pushes the given file to a location on the android device, that can be accessed by the PGConnect app.
        """
        self.driver.push_file(destination_path="/sdcard/Android/data/de.proglove.connect/files/{0}".format(
            file_name_on_destination), source_path=source_path)

    def relaunch_pg_app(self):
        # Closing App and relaunching it, User data will be kept.
        self.driver.close_app()
        time.sleep(3)
        self.driver.start_activity(pgconnect_package, pgconnect_launch_activity)

    def mirror_android_device_screen(self, udid=""):
        """
        Mirrors the screen of the android device under test to the desktop using scrcpy.
        """
        subprocess.Popen("scrcpy -s {}".format(udid), shell=True,
                         stderr=subprocess.STDOUT, preexec_fn=os.setsid)
        time.sleep(5)
