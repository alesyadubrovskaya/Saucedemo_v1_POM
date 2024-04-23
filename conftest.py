import pytest
from selenium import webdriver

from pages.auth_page import AuthPage, login
from pages.menu_page import SidebarPage
from pages.inventory_page import InventoryPage
from pages.filter_page import FilterPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

from locators.urls import URLs


@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--windows-size=1280,1000')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')

    browser = webdriver.Chrome(options=chrome_options)

    yield browser
    browser.quit()


@pytest.fixture()
def log_page(browser):
    log_page = AuthPage(browser, URLs.auth_url)
    return log_page


@pytest.fixture()
def inv_page(browser):
    inv_page = InventoryPage(browser, URLs.inventory_url)
    return inv_page


@pytest.fixture()
def menu_page(browser, login):
    menu_page = SidebarPage(browser, login)
    return menu_page


@pytest.fixture()
def filter_page(browser, login):
    filter_page = FilterPage(browser, login)
    return filter_page

@pytest.fixture()
def cart_page(browser):
    cart_page = CartPage(browser, URLs.cart_url)
    return cart_page


@pytest.fixture()
def item_page(browser, login):
    item_page = ItemPage(browser, login)
    return item_page


@pytest.fixture()
def order_page(browser):
    order_page = OrderPage(browser, URLs.checkout_url)
    return order_page


@pytest.fixture()
def about_page(browser):
    about_page = SidebarPage(browser, URLs.about_url)
    return about_page