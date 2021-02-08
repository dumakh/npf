from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, '[tabindex="1"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[tabindex="2"]')
    SIGN_IN = (By.ID, "kc-login")

class WidgetPageLocators(object):
    FL_NEWFACE_1 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-icon')
    FL_NEWFACE_2 = (By.CSS_SELECTOR, 'widget-form :nth-child(1) .header .menu-drop-list .menu-item:nth-child(2)')

