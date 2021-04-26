from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '14.4'
desired_caps['deviceName'] = 'iPhone 11'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = '/Users/candichiu/Documents/iOSAutomation/UICatalog.app'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_element_by_accessibility_id("Date Picker")

print("Is displayed: ", element.is_displayed())
print("Is enabled: ", element.is_enabled())
print("Is selected: ", element.is_selected())
print("Size: ", element.size)
print("Location: ", element.location)
