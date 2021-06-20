from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'Galaxy S10e'
        desired_caps['appPackage'] = 'com.samsung.android.calendar'
        desired_caps['appActivity'] = 'com.samsung.android.app.calendar.activity.MainActivity'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        return driver
