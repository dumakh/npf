from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, '[tabindex="1"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[tabindex="2"]')
    SIGN_IN = (By.ID, "kc-login")
    PROFILE = (By.CSS_SELECTOR, '.profile-brief .name')


class WidgetPageLocators(object):
    FL_NEWFACE_1 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-icon')
    FL_NEWFACE_2 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-drop-list .menu-item:nth-child(2)')
    NEW_FL = (By.XPATH, '//div[contains(text(), "Физические  лица")]')
    FL_JOURNAL_1 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-icon')
    FL_JOURNAL_2 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-drop-list .menu-item:nth-child(1)')
    FL_JOURNAL = (By.XPATH, '//div[contains(text(), "Журнал физических  лиц")]')


class CreateFlLocators(object):
    SURNAME = (By.CSS_SELECTOR, '[formcontrolname="surname"]')
    NAME = (By.CSS_SELECTOR, '[formcontrolname="name"]')
    PATRONOMIC = (By.CSS_SELECTOR, '[formcontrolname="patronymic"]')
    BIRTHDATE = (By.CSS_SELECTOR, '[formcontrolname="birthDate"]')
    GENDER = (By.CSS_SELECTOR, '[formcontrolname="gender"]')
    CREATE = (By.CSS_SELECTOR, '.buttons .positive')
    CREATE_SUCCESS = (By.CSS_SELECTOR, '[notification-type = "Success"]')
