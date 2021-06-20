import unittest
import pytest

from AppiumFrameWork.pages.calendar_page import CalendarCase


@pytest.mark.usefixtures("beforeClass", "setUp")
class CalendarTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cc = CalendarCase(self.driver)

    @pytest.mark.run(order=2)
    def test_search_event(self):
        self.cc.click_menu()
        self.cc.click_search()
        self.cc.take_screenshot()

    @pytest.mark.run(order=1)
    def test_create_event(self):
        self.cc.click_menu()
        self.cc.click_day()
        self.cc.add_event()
        self.cc.enter_event_title()
        self.cc.click_save()
