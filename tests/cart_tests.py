import pytest
from pages.auth_page import login
from locators.urls import URLs
from locators.item_locate import ItemData


# choose item via name and add/delete it via item page
@pytest.mark.positive
def test_add_item_mp(browser, login, inv_page, item_page, cart_page):
    inv_page.invent_names_find()[2].click()
    assert browser.current_url == URLs.item_url_3, 'Wrong URL'
    assert item_page.item_name_find().text == ItemData.item3_name, 'Wrong name'
    assert item_page.item_img_find().get_attribute('src') == ItemData.item3_img, 'Wrong image'
    assert item_page.item_price_find().text == ItemData.item3_price, 'Wrong price'
    item_page.item_add_find().click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item3_name, 'Wrong name'