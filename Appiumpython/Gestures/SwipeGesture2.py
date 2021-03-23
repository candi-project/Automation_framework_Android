from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'moto x4'
#desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
desired_caps['appPackage'] = 'de.ottonova.mobile'
desired_caps['appActivity'] = 'de.ottonova.mobile.main.MainActivity'
desired_caps['noReset'] = 'True'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

print("Device Width and Height: ", driver.get_window_size())
#Device Width and Height:  {'width': 1080, 'height': 1776}
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

#Swipe from Right to left
startx = screenWidth*7/10
endsx = 0
starty = screenHeight*3/10
endsy = screenHeight*3/10

#Swipe from Top to Buttom
startx2 = screenWidth/2
endsx2 = screenWidth/2
starty2 = screenHeight*2/9
endsy2 = screenHeight*8/9

time.sleep(3)
actions = TouchAction(driver)
for x in range(7):
    actions.long_press(None, startx, starty).move_to(None, endsx, endsy).release().perform()
    time.sleep(3)

# actions.long_press(None, startx2, starty2).move_to(None, endsx2, endsy2).release().perform()


