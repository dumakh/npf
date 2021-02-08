from pages.main_page import MainPage
import time
from selenium.webdriver.support.ui import WebDriverWait

def test_sign_account(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.sign_account()
    time.sleep(1)

def test_widget_fl_newface(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.sign_account()
    time.sleep(2)
    page.new_face_on_widget_fl()
    time.sleep(2)