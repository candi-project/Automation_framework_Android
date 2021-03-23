from appium import webdriver
from AppiumFrameWork.base.DriverClass import Driver
from AppiumFrameWork.pages.welcome_event_page import WelcomeEventPage
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.utilities.constants import *
import time

dr = Driver()
driver = dr.getDriverMethod()
time.sleep(2)

# source = driver.page_source
# print(source)
wp = WelcomeEventPage(driver)
# wp.welcome_page_verify()
# wp.click_send_app_usage()
# wp.click_test_app()
# time.sleep(6)
# wp.press_back_button_twice()
# wp.event_card_title()
# wp.swipe_event_card()
wp.count_event_card_print_title()

time.sleep(3)
# source = driver.page_source
# print(source)