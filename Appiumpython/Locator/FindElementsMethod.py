from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'moto x4'
desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
desired_caps['appPackage'] = 'de.proglove.connect'
desired_caps['appActivity'] = 'de.proglove.connect.app.main.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub" ,desired_caps)

scan2pair = driver.find_element_by_android_uiautomator('text("SCAN2PAIR")').click()
elements = driver.find_elements_by_class_name("android.widget.Button")

for x in elements:
    print(x.text)

for x in elements:
    button = x.text
    if button == "CANCEL":
        x.click()
    break

time.sleep(5)

driver.quit()