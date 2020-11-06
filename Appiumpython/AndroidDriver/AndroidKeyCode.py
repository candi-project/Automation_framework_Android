from appium import webdriver
import time

#https://stackoverflow.com/questions/11768356/need-table-of-key-codes-for-android-and-presenter

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'moto x4'
desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
desired_caps['appPackage'] = 'de.proglove.connect'
desired_caps['appActivity'] = 'de.proglove.connect.app.main.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub" ,desired_caps)

ele_id = driver.find_element_by_id("de.proglove.connect:id/proximityInfoFragment")
ele_id.click()

ele_textvalue = driver.find_element_by_android_uiautomator('text("OKAY")')
ele_textvalue.click()

time.sleep(2)
driver.press_keycode(4)
time.sleep(2)
driver.press_keycode(3)

