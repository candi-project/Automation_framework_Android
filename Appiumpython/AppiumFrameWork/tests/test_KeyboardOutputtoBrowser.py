import unittest
import pytest

from AppiumFrameWork.pages.KeyboardOutputtoBrowser import KeyboardOutputtoBrowser


@pytest.mark.usefixtures("beforeClass", "setUp")
class KeyboardOutputtoBrowserTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.kb = KeyboardOutputtoBrowser(self.driver)

    @pytest.mark.run(order=2)
    def test_google_chrome(self):
        self.kb.switch_to_Google_Chrome()
        self.kb.message()
        self.kb.scan_displayed_barcode()

    @pytest.mark.run(order=1)
    def test_pg_app(self):
        self.kb.push_config_file_to_mobile()
        self.kb.resolve_keyboard_requirement()
        self.kb.click_pairing_btn()
        self.kb.allow_access_location()
        self.kb.allow_access_location_system()

