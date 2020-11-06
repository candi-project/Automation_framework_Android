from appium import webdriver

class Driver:
    def getDriverMethod(self):
        #Insight Mobile App
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '9'
        # desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['deviceName'] = 'moto x4'
        # desired_caps['app'] = ('/home/candi/Downloads/PgConnect_release_1.7.0_270820_1004.apk')
        # desired_caps['appPackage'] = 'de.proglove.connect'
        # desired_caps['appActivity'] = 'de.proglove.connect.app.main.MainActivity'

        #Android Demo App
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'moto x4'
        desired_caps['app'] = ('/home/candi/Desktop/Android/Appium/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://localhost:4723/wd/hub" ,desired_caps)

        return driver


