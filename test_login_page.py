from pages.main_page import MainPage
import time

def test_sign_account(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.sign_account()
    time.sleep(1)