import pytest
from pages.auth_page import login
from locators.urls import URLs
from locators.item_locate import ItemData


# choose item via name and add/delete it via item page
@pytest.mark.positive
def test_add_item_ip_1(browser, login, inv_page, item_page, cart_page):
    inv_page.invent_names_find()[2].click()
    assert browser.current_url == URLs.item_url_3, 'Wrong URL'
    assert item_page.item_name_find().text == ItemData.item3_name, 'Wrong name'
    assert item_page.item_img_find().get_attribute('src') == ItemData.item3_img, 'Wrong image'
    assert item_page.item_price_find().text == ItemData.item3_price, 'Wrong price'
    item_page.item_add_find().click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    cart_page.cart_icon_find().click()
    assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item3_name, 'Wrong name'
    item_page.go_back()
    item_page.item_remove_find().click()
    assert cart_page.cart_badge_invisible(), 'Wrong quantity'


# choose item via image, add it via item page and delete it via cart page
@pytest.mark.positive
def test_add_item_ip_2(browser, login, inv_page, item_page, cart_page):
    inv_page.invent_imgs_find()[4].click()
    assert browser.current_url == URLs.item_url_5, 'Wrong URL'
    assert item_page.item_name_find().text == ItemData.item5_name, 'Wrong name'
    assert item_page.item_img_find().get_attribute('src') == ItemData.item5_img, 'Wrong image'
    assert item_page.item_price_find().text == ItemData.item5_price, 'Wrong price'
    item_page.item_add_find().click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    cart_page.cart_icon_find().click()
    assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item5_name, 'Wrong name'
    cart_page.cart_remove_find().click()
    assert cart_page.cart_badge_invisible(), 'Wrong quantity'


# add/delete item via main page
@pytest.mark.positive
def test_add_item_mp(browser, login, inv_page, item_page, cart_page):
    inv_page.invent_adds_find()[0].click()
    assert browser.current_url == URLs.inventory_url, 'Wrong URL'
    assert inv_page.invent_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    assert inv_page.invent_imgs_find()[0].get_attribute('src') == ItemData.item1_img, 'Wrong image'
    assert inv_page.invent_prices_find()[0].text == ItemData.item1_price, 'Wrong price'
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    cart_page.cart_icon_find().click()
    assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    cart_page.cart_return().click()
    inv_page.invent_removes_find()[0].click()
    assert cart_page.cart_badge_invisible(), 'Wrong quantity'

