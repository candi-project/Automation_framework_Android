import time

from appium import webdriver

# http://appium.io/docs/en/writing-running-appium/web/hybrid/
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '14.4'
desired_caps['deviceName'] = 'iPhone 11'
desired_caps['automationName'] = 'XCUITest'
desired_caps['autoWebview'] = 'true'
desired_caps['browserName'] = 'safari'

# desired_caps['app'] = '/Users/candichiu/Documents/iOSAutomation/UICatalog.app'

# 1.) Create driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2.) Explict Wait object
wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])
# 3.) Launch URL
driver.get("http://dummypoint.com/seleniumtemplate.html")

# 4.) Perform the testing on the URL
time.sleep(2)
enterText = wait.until(lambda x: x.find_element_by_id("user_input"))
enterText.click()
enterText.send_keys("Candi")

submit = wait.until(lambda x: x.find_element_by_id("submitbutton"))
submit.click()

# 5.) Quit the driver
time.sleep(10)
driver.quit()
