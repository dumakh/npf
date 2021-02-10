from .base_page import BasePage
from .locators import MainPageLocators, WidgetPageLocators, CreateFlLocators
from selenium.webdriver.common.action_chains import ActionChains
from .random import RandomEl, ManName, WomanName
from selenium.webdriver.common.keys import Keys
from .result import ResultPage
import time

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def sign_account(self):
        self.browser.find_element(*MainPageLocators.LOGIN_USERNAME).send_keys("realm1user1")
        self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys("realm1user1pwd")
        self.browser.find_element(*MainPageLocators.SIGN_IN).click()


    def new_face_on_widget_fl(self):
        self.browser.find_element(*WidgetPageLocators.FL_NEWFACE_1).click()
        self.browser.find_element(*WidgetPageLocators.FL_NEWFACE_2).click()


    def journal_on_widget_fl(self):
        self.browser.find_element(*WidgetPageLocators.FL_JOURNAL_1).click()
        self.browser.find_element(*WidgetPageLocators.FL_JOURNAL_2).click()


    def create_fl_man(self):
        self.browser.find_element(*CreateFlLocators.SURNAME).click()
        self.browser.find_element(*CreateFlLocators.SURNAME).send_keys(*ManName.rand_surname)
        self.browser.find_element(*CreateFlLocators.NAME).click()
        self.browser.find_element(*CreateFlLocators.NAME).send_keys(*ManName.rand_name)
        self.browser.find_element(*CreateFlLocators.PATRONOMIC).click()
        self.browser.find_element(*CreateFlLocators.PATRONOMIC).send_keys(*ManName.rand_patr)
        self.browser.find_element(*CreateFlLocators.BIRTHDATE).click()
        self.browser.find_element(*CreateFlLocators.BIRTHDATE).send_keys(*RandomEl.rand_date)
        self.browser.find_element(*CreateFlLocators.CREATE).click()


    def create_fl_woman(self):
        actions = ActionChains(self.browser)
        self.browser.find_element(*CreateFlLocators.SURNAME).click()
        self.browser.find_element(*CreateFlLocators.SURNAME).send_keys(*WomanName.rand_surname)
        self.browser.find_element(*CreateFlLocators.NAME).click()
        self.browser.find_element(*CreateFlLocators.NAME).send_keys(*WomanName.rand_name)
        self.browser.find_element(*CreateFlLocators.PATRONOMIC).click()
        self.browser.find_element(*CreateFlLocators.PATRONOMIC).send_keys(*WomanName.rand_patr)
        self.browser.find_element(*CreateFlLocators.GENDER).click()
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.browser.find_element(*CreateFlLocators.BIRTHDATE).click()
        self.browser.find_element(*CreateFlLocators.BIRTHDATE).send_keys(*RandomEl.rand_date)
