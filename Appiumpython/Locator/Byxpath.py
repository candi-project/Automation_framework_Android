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

#ele_xpath = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]')
#ele_xpath = driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="de.proglove.connect:id/homeFragment"]')
#ele_xpath = driver.find_element_by_xpath('//android.widget.ImageView[@index="0"]')

# ele_textvalue = driver.find_element_by_android_uiautomator('text("SCAN2PAIR")')
# ele_textvalue.click()

#ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@text="CANCEL"]')

ele_xpath1 = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Proximity"]')
ele_xpath1.click()

ele_xpath = driver.find_element_by_xpath('//android.widget.Button')
ele_xpath.click()