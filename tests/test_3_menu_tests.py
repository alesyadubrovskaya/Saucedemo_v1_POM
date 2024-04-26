import pytest
import allure
from pages.auth_page import login
from locators.urls import URLs


@allure.id('3_1')
@allure.epic('Sidebar')
@allure.feature('sidebar')
@allure.title('account logout')
@pytest.mark.positive
def test_logout(browser, login, log_page, menu_page):
    with allure.step('click the logout option in the sidebar'):
        menu_page.open_menu().click()
        menu_page.logout_opt().click()
    with allure.step('check the current url and login button'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        log_btn = log_page.btn_login()
        assert log_page.btn_login(), 'Login button not present'
        assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'


@allure.id('3_2')
@allure.epic('Sidebar')
@allure.feature('sidebar')
@allure.title('redirect to about page')
@pytest.mark.positive
def test_about(browser, login, menu_page, about_page):
    with allure.step('click the about option in the sidebar'):
        menu_page.open_menu().click()
        menu_page.about_opt().click()
    with allure.step('check the current url and the page title'):
        curr_title = browser.title
        assert browser.current_url == URLs.about_url and \
           curr_title == URLs.exp_title, 'Wrong URL or title'


@allure.id('3_3')
@allure.epic('Sidebar')
@allure.feature('sidebar')
@allure.title('reset app state')
@pytest.mark.positive
def test_reset(browser, login, inv_page, cart_page, menu_page):
    with allure.step('add goods to cart'):
        inv_page.invent_adds_find()[2].click()
        inv_page.invent_adds_find()[3].click()
    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 2, 'Wrong quantity'
    with allure.step('click the reset app state option in the sidebar'):
        menu_page.open_menu().click()
        menu_page.reset_opt().click()
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Cart not empty'
    cart_page.refresh()


@allure.id('3_4')
@allure.epic('Sidebar')
@allure.feature('sidebar')
@allure.title('redirect to inventory page')
@pytest.mark.positive
def test_allitems(browser, login, inv_page, item_page, menu_page):
    with allure.step('go to item page'):
        inv_page.invent_names_find()[1].click()
    with allure.step('check the current url'):
        assert browser.current_url == URLs.item_url_2
    with allure.step('click the all items option in the sidebar'):
        menu_page.open_menu().click()
        menu_page.allitem_opt().click()
    with allure.step('check current url'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'