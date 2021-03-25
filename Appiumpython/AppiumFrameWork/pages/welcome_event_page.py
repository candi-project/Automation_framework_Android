import time

from appium.webdriver.common.touch_action import TouchAction

from AppiumFrameWork.base.BasePage import BasePage
from urllib.parse import urlparse


class WelcomeEventPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values
    _app_usage_data = "App usage data"  # text
    _send_app_usage_data = "Send app usage data"  # text
    _test_app = "Test app"  # text
    _appointment = "de.ottonova.mobile:id/timelineFabButton"  # id
    _events = "Events"  # text
    _event_cards = "de.ottonova.mobile:id/message"  # id
    _profile = "Profile"  # text
    _tool_bar_menu = "de.ottonova.mobile:id/ottoToolbarMenuContainer"  # id
    _our_tariffs = "Our Tariffs"  # text
    _full_insurance = "FULL INSURANCE"  # text
    _tariff_list = "de.ottonova.mobile:id/detail_container"  # id
    _aid_insurance = "AID INSURANCE"  # text
    _calculate_premium = "Calculate premium"  # text
    _tariff_icon = "de.ottonova.mobile:id/tariffIcon"  # id

    def welcome_page_verify(self):
        self.isDisplayed(self._app_usage_data, "text")

    def click_send_app_usage(self):
        self.clickElement(self._send_app_usage_data, "text")

    def click_test_app(self):
        self.clickElement(self._test_app, "text")

    def event_page_verify(self):
        self.getElement(self._appointment, "id")

    def press_back_button(self):
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

    def click_profile(self):
        self.clickElement(self._profile, "text")

    def verify_profile(self):
        self.isDisplayed(self._tool_bar_menu, "id")

    def click_our_tariff(self):
        self.clickElement(self._our_tariffs, "text")

    def verify_our_tariff(self):
        # self.isDisplayed(self._tariff_list, "text")
        self.isDisplayed(self._full_insurance, "text")
        self.isDisplayed(self._aid_insurance, "text")

    def click_calculate_premium(self):
        self.clickElement(self._calculate_premium, "text")

    def get_url(self):
        time.sleep(5)
        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)
        url = self.driver.current_url
        self.driver.switch_to.context('NATIVE_APP')
        return url

    def verify_url(self):
        expected_url = "https://www.ottonova.de/online-beitragsrechner/?utm_source=content_referral&utm_medium" \
                       "=ottonova_app&utm_campaign=tariff "
        a_url = urlparse(expected_url)
        b_url = urlparse(self.get_url())
        match = a_url.netloc == b_url.netloc
        if match == True:
            print("The URL is equal to expected URL.")
        else:
            print("The URL is not equal to expected URL.")
            assert False
