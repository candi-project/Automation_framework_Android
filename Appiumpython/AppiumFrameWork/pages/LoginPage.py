
import AppiumFrameWork.utilities.CustomLogger as cl

from AppiumFrameWork.base.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Login Page.
    _loginButton = "LOGIN" #text
    _enterEmail = "Enter Email" #text
    _enterPassword = "Enter Password" #text
    _clickOnLoginBtn = "com.code2lead.kwad:id/Btn3" #id
    _pageTitle = "Enter Admin" #text
    _enterAdmin = "com.code2lead.kwad:id/Edt_admin" #id
    _submitBtn = "SUBMIT" #text

    def clickLoginBtn(self):
        #self.waitForElement(self._loginButton, "text")
        self.clickElement(self._loginButton, "text")
        cl.allureLogs("Clicked on Login Button.")

    def enterEmail(self):
        self.sendText("admin@gmail.com", self._enterEmail, "text")
        cl.allureLogs("Entered Email.")

    def enterPassword(self):
        self.sendText("admin123", self._enterPassword,"text")
        cl.allureLogs("Entered Password.")

    def enterPassword2(self):
        self.sendText("admin1234", self._enterPassword,"text")
        cl.allureLogs("Entered Password.")

    def clickOnLoginBtn(self):
        self.clickElement(self._clickOnLoginBtn, "id")
        cl.allureLogs("Clicked on Login Button.")

    def verifyAdminScreen(self):
        self.isDisplayed(self._pageTitle,"text")
        #assert adminscreen == True
        cl.allureLogs("Opened admin screen.")

    def enterAdmin(self):
        self.sendText("Candi", self._enterAdmin, "id")
        cl.allureLogs("Entered admin.")

    def clickOnSubmit(self):
        self.clickElement(self._submitBtn, "text")
        cl.allureLogs("Clicked on Submit Button.")

    def scrollAndClick(self):
        self.scrollElement(self._loginButton, "text")
        cl.allureLogs("Scrolled to Login Button and Clicked on it.")