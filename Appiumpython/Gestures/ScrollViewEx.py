from appium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'moto x4'
desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
desired_caps['appPackage'] = 'de.proglove.connect'
desired_caps['appActivity'] = 'de.proglove.connect.app.main.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub" ,desired_caps)

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
ele1 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]').click()
ele2 = driver.find_element_by_android_uiautomator('text("Switch to Foreman View")').click()

wait.until(lambda x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Firmware Update"))')).click()

driver.quit()