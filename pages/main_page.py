from .base_page import BasePage
from .locators import MainPageLocators
from .locators import WidgetPageLocators

class MainPage(BasePage):
    def sign_account(self):
        email_field = self.browser.find_element(*MainPageLocators.LOGIN_USERNAME).send_keys("realm1user1")
        password_field = self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys("realm1user1pwd")
        self.browser.find_element(*MainPageLocators.SIGN_IN).click()

    def new_face_on_widget_fl(self):
        self.browser.find_element(*WidgetPageLocators.FL_NEWFACE_1).click
        self.browser.find_element(*WidgetPageLocators.FL_NEWFACE_2).click