from .base_page import BasePage
from .locators import MainPageLocators, WidgetPageLocators, CreateFlLocators


class ResultPage(BasePage):

    def should_be_profile(self):
        assert self.is_element_present(*MainPageLocators.PROFILE), "Error login"

    def should_be_new_fl(self):
        assert self.is_element_present(*WidgetPageLocators.NEW_FL), "Ошибка входа на создание нового ФЛ с виджета"

    def should_be_journal_fl(self):
        assert self.is_element_present(*WidgetPageLocators.FL_JOURNAL), "Ошибка входа в журнал ФЛ с виджета"

    def should_be_create(self):
        assert self.is_element_present(*CreateFlLocators.CREATE_SUCCESS), "Ошибка создания"
