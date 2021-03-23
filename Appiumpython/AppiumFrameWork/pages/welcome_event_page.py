import time

from appium.webdriver.common.touch_action import TouchAction

from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl


class WelcomeEventPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values
    _app_usage_data = "App usage data"  # text
    _send_app_usage_data = "Send app usage data"  # text
    _test_app = "Test app"  # text
    _appointment = "de.ottonova.mobile:id/timelineFabButton"  # id
    _event_cards = "de.ottonova.mobile:id/message"  # id

    def welcome_page_verify(self):
        self.isDisplayed(self._app_usage_data, "text")

    def click_send_app_usage(self):
        self.clickElement(self._send_app_usage_data, "text")

    def click_test_app(self):
        self.clickElement(self._test_app, "text")

    def event_page_verify(self):
        self.isDisplayed(self._appointment, "id")

    def press_back_button_twice(self):
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)

    def event_card_title(self):
        title = self.getElement(self._event_cards, "id").text
        # print("Event card title: ", title)
        return title

    def swipe_event_card(self):
        # print("Device Width and Height: ", self.driver.get_window_size())
        device_size = self.driver.get_window_size()
        screen_width = device_size['width']
        screen_height = device_size['height']

        # Swipe from Right to left
        startx = screen_width * 7 / 10
        endsx = 0
        starty = screen_height * 3 / 10
        endsy = screen_height * 3 / 10

        if self.isDisplayed(self._event_cards, "id"):
            actions = TouchAction(self.driver)
            actions.long_press(None, startx, starty).move_to(None, endsx, endsy).release().perform()

    def count_event_card_print_title(self):
        card_number = 0
        a = []
        loop = True
        while loop:
            a.append(self.event_card_title())
            self.swipe_event_card()
            for i in range(len(a) - 1):
                if a[i] == a[i + 1]:
                    print("Total Card Number:", card_number)
                    a.remove(a[i])
                    print(*a, sep="\n")
                    loop = False
                    break
            card_number += 1