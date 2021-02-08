import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import CartPage
from urllib.parse import urlparse
import time

class TestWidgetNewface(object):
    link = "http://npf.bivgroup.com/"
    page = MainPage(browser, link)
    page.open()
    page.sign_account()
    time.sleep(1)