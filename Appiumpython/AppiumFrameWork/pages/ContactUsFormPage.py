from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl

class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "Enter Mobile No"  # text
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Clicked on Contact us form button.")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Contact Us Form Page opened.")

    def enterName(self):
        self.sendText("Code2Lead",self._enterName,"text")
        cl.allureLogs("Enter Name")

    def enterEmail(self):
        self.sendText("abc@gmail.com",self._enterEmail,"text")
        cl.allureLogs("Enter Email")

    def enterAddress(self):
        self.sendText("Taiwan",self._enterAddress,"text")
        cl.allureLogs("Enter Address")

    def enterMNumber(self):
        self.sendText("987654210", self._enterMobileNumber, "text")
        cl.allureLogs("Enter Mobile Number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit Button.")






