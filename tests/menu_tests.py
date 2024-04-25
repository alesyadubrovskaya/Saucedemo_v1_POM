import pytest
from pages.auth_page import login
from locators.urls import URLs


# logout option test
@pytest.mark.positive
def test_logout(browser, login, log_page, menu_page):
    menu_page.open_menu().click()
    menu_page.logout_opt().click()
    assert browser.current_url == URLs.auth_url, 'Wrong URL'
    log_btn = log_page.btn_login()
    assert log_page.btn_login(), 'Login button not present'
    assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'


# about option test
@pytest.mark.positive
def test_about(browser, login, menu_page, about_page):
    menu_page.open_menu().click()
    menu_page.about_opt().click()
    curr_title = browser.title
    assert browser.current_url == URLs.about_url and \
           curr_title == URLs.exp_title, 'Wrong URL or title'


# reset option test
@pytest.mark.positive
def test_reset(browser, login, inv_page, cart_page, menu_page):
    inv_page.invent_adds_find()[2].click()
    inv_page.invent_adds_find()[3].click()
    assert int(cart_page.cart_badge_visible().text) == 2, 'Wrong quantity'
    menu_page.open_menu().click()
    menu_page.reset_opt().click()
    assert cart_page.cart_badge_invisible(), 'Cart not empty'
    cart_page.refresh()


# allitems option test
@pytest.mark.positive
def test_allitems(browser, login, inv_page, item_page, menu_page):
    inv_page.invent_names_find()[1].click()
    assert browser.current_url == URLs.item_url_2
    menu_page.open_menu().click()
    menu_page.allitem_opt().click()
    assert browser.current_url == URLs.inventory_url, 'Wrong URL'