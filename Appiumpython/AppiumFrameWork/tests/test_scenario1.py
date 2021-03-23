import unittest
import pytest

from AppiumFrameWork.pages.welcome_event_page import WelcomeEventPage


@pytest.mark.usefixtures("beforeClass")
class Scenario1(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.we = WelcomeEventPage(self.driver)

    @pytest.mark.run(order=2)
    def test_welcome_page(self):
        self.we.welcome_page_verify()
        self.we.click_send_app_usage()

    @pytest.mark.run(order=3)
    def test_test_app(self):
        self.we.click_test_app()
        self.we.event_page_verify()

    @pytest.mark.run(order=4)
    def test_event_card_numer_title(self):
        self.we.press_back_button_twice()
        self.we.count_event_card_print_title()
