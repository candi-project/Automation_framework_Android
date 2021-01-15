from appium import webdriver
from AppiumFrameWork.base.DriverClass import Driver
from AppiumFrameWork.pages.KeyboardOutputtoBrowser import KeyboardOutputtoBrowser
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.utilities.constants import *
import time

dr = Driver()
driver = dr.getDriverMethod(pgconnect_package, pgconnect_launch_activity)
#time.sleep(2)
driver.reset()

# bp = BasePage(driver)


re = KeyboardOutputtoBrowser(driver)
re.push_config_file_to_mobile()
re.resolve_keyboard_requirement()
re.click_pairing_btn()
re.allow_access_location()
re.allow_access_location_system()
re.switch_to_Google_Chrome()
re.Message()
re.scan_displayed_barcode()

time.sleep(3)


