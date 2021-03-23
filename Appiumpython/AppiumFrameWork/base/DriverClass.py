from appium import webdriver



class Driver:
    def getDriverMethod(self):
        # Insight Mobile App
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'moto x4'
        #desired_caps['app'] = (
        #     '/home/candi/Desktop/Android/Insight_Mobile_Official_Release/InsightMobile_release_1.9.0_081220_1607.apk')
        desired_caps['appPackage'] = 'de.ottonova.mobile'
        desired_caps['appActivity'] = 'de.ottonova.mobile.main.MainActivity'
        #desired_caps['newCommandTimeout'] = 600
        #desired_caps['noReset'] = 'True'


        # Android Demo App
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '9'
        # desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['deviceName'] = 'moto x4'
        # desired_caps['app'] = ('/home/candi/Desktop/Android/Appium/Android_Demo_App.apk')
        # desired_caps['appPackage'] = 'com.code2lead.kwad'
        # desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        return driver
