import time
import unittest
import pytest

from AppiumFrameWork.pages.welcome_event_page import WelcomeEventPage


@pytest.mark.usefixtures("beforeClass")
class Scenario2(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.we = WelcomeEventPage(self.driver)

    @pytest.mark.run(order=2)
    def test_welcome_page_to_test_app(self):
        self.we.welcome_page_verify()
        self.we.click_send_app_usage()
        self.we.click_test_app()
        self.we.event_page_verify()
        for i in range(2):
            self.we.press_back_button()
            time.sleep(1)

    @pytest.mark.run(order=3)
    def test_profile(self):
        self.we.click_profile()
        self.we.press_back_button()
        self.we.verify_profile()

    @pytest.mark.run(order=4)
    def test_our_tariffs(self):
        self.we.click_our_tariff()
        self.we.verify_our_tariff()

    @pytest.mark.run(order=5)
    def test_calculate_premium(self):
        self.we.click_calculate_premium()
        self.we.get_url()
        self.we.verify_url()

