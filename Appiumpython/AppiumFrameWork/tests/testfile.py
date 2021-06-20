from appium import webdriver
from AppiumFrameWork.base.DriverClass import Driver
from AppiumFrameWork.pages.calendar_page import CalendarCase
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.utilities.constants import *
import time

dr = Driver()
driver = dr.getDriverMethod()
#time.sleep(2)
#driver.reset()

# bp = BasePage(driver)
cla = CalendarCase(driver)
# cla.click_menu()
# cla.click_day()
# cla.add_event()
# cla.enter_event_title()
# cla.click_save()
cla.click_menu()
cla.click_search()
cla.take_screenshot()


# re = KeyboardOutputtoBrowser(driver)
# re.push_config_file_to_mobile()
# re.resolve_keyboard_requirement()
# re.click_pairing_btn()
# re.allow_access_location()
# re.allow_access_location_system()
# re.switch_to_Google_Chrome()
# re.Message()
# re.scan_displayed_barcode()
#
# time.sleep(3)


