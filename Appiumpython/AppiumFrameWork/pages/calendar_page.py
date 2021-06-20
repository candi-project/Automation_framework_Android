from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl


class CalendarCase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _menu_button = "com.samsung.android.calendar:id/open_drawer_badge"  # id
    _day = "Day"  # text
    _add_event = "com.samsung.android.calendar:id/floating_action_button"  # id
    _event_title = "com.samsung.android.calendar:id/title"  # id
    _save_button = "com.samsung.android.calendar:id/add_app_bar_menu_done"  # id
    _search = "Search"  # text
    _background_container = "com.samsung.android.calendar:id/background_container"  # id

    def click_menu(self):
        self.clickElement(self._menu_button, "id")
        cl.allureLogs("Clicked on menu button.")

    def click_day(self):
        self.clickElement(self._day, "text")
        cl.allureLogs("Clicked on Day tab.")

    def add_event(self):
        self.clickElement(self._add_event, "id")
        cl.allureLogs("Clicked on Add_Event button.")

    def enter_event_title(self):
        self.sendText("kfz24_tech_task", self._event_title, "id")
        cl.allureLogs("Entered TiTle.")

    def click_save(self):
        self.clickElement(self._save_button, "id")
        cl.allureLogs("Saved Event.")

    def click_search(self):
        self.clickElement(self._search, "text")
        cl.allureLogs("Clicked Search.")

    def take_screenshot(self):
        assert self.isDisplayed(self._background_container)
        if self.getElement(self._event_title).text == "kfz24_tech_task":
            self.clickElement(self._event_title)
            self.takeScreenShot('kfz24_tech_task')
            self.screenShot('kfz24_tech_task')
