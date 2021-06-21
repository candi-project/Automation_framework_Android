## Automation_framework_Android
Branch-kfzteile24

## Suggested environment
Pycharm/python3

## SetUp
1. Clone this branch-kfzteile24 to local device.
2. Install requirement.txt `pip3 install -r RequirementSetUp.txt`
3. Install Appium from here. [appium desktop](https://github.com/appium/appium-desktop/releases/tag/v1.21.0)
4. Modify desired capability from `DriverClass.py`. 
**deviceName/platformVersion/appPackage/appActivity must be updated according to your device.**
```
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Galaxy S10e'
desired_caps['appPackage'] = 'com.samsung.android.calendar'
desired_caps['appActivity'] = 'com.samsung.android.app.calendar.activity.MainActivity'
```
5. Make sure Appium server is running.
6. Under Appiumpython/AppiumFrameWork/tests folder, 
enter `py.test --alluredir="PATH_TO_WHERE_YOU_WOULD_LIKE_TO_SAVE_ALLURE_REPORT" test_calendar_page.py`

## Report
Once test is done, Open terminal and type 
`allure serve 'PATH_WHERE_YOU_SAVED_ALLURE_REPORT'`

**Note: Suggested setting allure $path variable to .zshrc or .bashrc according to your environment.** 
