from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '14.4'
desired_caps['deviceName'] = 'iPhone 11'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = '/Users/candichiu/Documents/iOSAutomation/UICatalog.app'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

print("Check if device is locked or not:", driver.is_locked())
print("Current context: ", driver.current_context)
print("Current orientation: ", driver.orientation)
