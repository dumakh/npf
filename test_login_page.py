from .pages.main_page import MainPage




def test_sign_account(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.sign_account()
    page.result.should_be_profile


def test_widget_fl_newface(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)
    page.open()
    page.sign_account()
    page.new_face_on_widget_fl()
    page.result.should_be_new_fl()


def test_widget_fl_journal(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)
    page.open()
    page.sign_account()
    page.journal_on_widget_fl()
    page.result.should_be_journal_fl()


def test_create_new_fl_man(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)
    page.open()
    page.sign_account()
    page.new_face_on_widget_fl()
    page.create_fl_man()
    page.result.should_be_create()


def test_create_new_fl_woman(browser):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)
    page.open()
    page.sign_account()
    page.new_face_on_widget_fl()
    page.create_fl_woman()
    page.result.should_be_create()
