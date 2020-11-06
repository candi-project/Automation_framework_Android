from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'moto x4'
desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
desired_caps['appPackage'] = 'de.proglove.connect'
desired_caps['appActivity'] = 'de.proglove.connect.app.main.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub" ,desired_caps)

element = driver.find_element_by_class_name("android.widget.FrameLayout")

print("Is displayed: ", element.is_displayed())
print("Is enabled: ", element.is_enabled())
print("Is selected: ", element.is_selected())
print("Size: ", element.size)
print("Location: ", element.location)