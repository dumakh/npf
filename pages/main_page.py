from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def sign_account(self):
        email_field = self.browser.find_element(*MainPageLocators.LOGIN_USERNAME).send_keys("realm1user1")
        password_field = self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys("realm1user1pwd")
        self.browser.find_element(*MainPageLocators.SIGN_IN).click()