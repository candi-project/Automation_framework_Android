from appium import webdriver



class Driver:
    def getDriverMethod(self):
        # Insight Mobile App
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'moto x4'
        desired_caps['appPackage'] = 'de.ottonova.mobile'
        desired_caps['appActivity'] = 'de.ottonova.mobile.main.MainActivity'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        return driver
