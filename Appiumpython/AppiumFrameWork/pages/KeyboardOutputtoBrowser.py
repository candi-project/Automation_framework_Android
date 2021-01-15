import os
import time
import matplotlib.pyplot as plt

from tkinter import messagebox
from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.utilities.constants import *
from AppiumFrameWork.base.DriverClass import Driver


class KeyboardOutputtoBrowser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values when launching app the first time.
    _access_location_okay = "de.proglove.connect:id/okayBtn"  # id
    _allow_insight_mobile_allow = "com.android.packageinstaller:id/permission_allow_button"  # id
    _scan2pair_btn = "de.proglove.connect:id/connectionButton"  # id
    _default_keyboard_choose = "de.proglove.connect:id/actionButton"  # id
    _ProGlove_keyboard = "ProGlove Keyboard"  # text
    _Google_search_box = "com.android.chrome:id/search_box_text"  # id

    def push_config_file_to_mobile(self):
        marker_auxiliary_dir = "/home/candi/PycharmProjects/Appiumpython/AppiumFrameWork"

        self.push_local_file_to_the_pgconnect_directory_on_the_device_under_test(
            os.path.join(
                marker_auxiliary_dir, "configurationfiles/KeyboardOutputtoBrowser.proconfig"
            ),
            "ProGlove.proconfig",
        )
        time.sleep(1)
        cl.allureLogs("Pushed a config file.")

    def resolve_keyboard_requirement(self):
        self.clickElement(self._default_keyboard_choose, "id")
        time.sleep(1)
        self.clickElement(self._ProGlove_keyboard, "text")
        cl.allureLogs("Resolved keyboard requirement.")

    def click_pairing_btn(self):
        self.clickElement(self._scan2pair_btn, "id")
        time.sleep(1)
        cl.allureLogs("Clicked pairing button-Scan2Pair.")

    def allow_access_location(self):
        self.clickElement(self._access_location_okay, "id")
        time.sleep(1)
        cl.allureLogs("Access location is allowed.")

    def allow_access_location_system(self):
        self.clickElement(self._allow_insight_mobile_allow, "id")
        cl.allureLogs("System location is allowed.")

        messagebox.showinfo("Action Required", "Please Press Ok and scan pairing barcode.")
        time.sleep(10)

    def switch_to_Google_Chrome(self):
        dr2 = Driver()
        self.driver2 = dr2.getDriverMethod(chrome_package, chrome_launch_activity)
        cl.allureLogs("Google Chrome app is launched.")

        self.driver2.reset()
        cl.allureLogs("Google Chrome app is reset.")
        time.sleep(3)

        self.clickElement(self._Google_search_box, "id")
        cl.allureLogs("Clicked Google search box.")

    def scan_displayed_barcode(self):
        img = plt.imread('/home/candi/PycharmProjects/Appiumpython/AppiumFrameWork/configurationfiles/testingbarcode'
                         '/ProGlove2.png')
        plt.imshow(img)
        cl.allureLogs("Barcode is displayed.")

        plt.pause(5)

        plt.close()
        cl.allureLogs("Barcode is closed.")

    def message(self):
        messagebox.showinfo("Action Required", "Please Press Ok and scan following barcode.")

