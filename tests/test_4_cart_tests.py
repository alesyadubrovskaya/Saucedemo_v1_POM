import pytest
import allure
from pages.auth_page import login
from locators.urls import URLs
from locators.item_locate import ItemData


@allure.id('4_1')
@allure.epic('CartAddRemove')
@allure.feature('item_add_remove')
@allure.title('item add and remove via item page')
@pytest.mark.positive
def test_add_item_ip_1(browser, login, inv_page, item_page, cart_page):
    with allure.step('go to the item page'):
        inv_page.invent_names_find()[2].click()
    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.item_url_3, 'Wrong URL'
        assert item_page.item_name_find().text == ItemData.item3_name, 'Wrong name'
        assert item_page.item_img_find().get_attribute('src') == ItemData.item3_img, 'Wrong image'
        assert item_page.item_price_find().text == ItemData.item3_price, 'Wrong price'
    with allure.step('add the item to the cart'):
        item_page.item_add_find().click()
    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()
    with allure.step('check the current url and item name'):
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item3_name, 'Wrong name'
    with allure.step('go back to the item page'):
        item_page.go_back()
    with allure.step('remove the item from the cart'):
        item_page.item_remove_find().click()
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Wrong quantity'


@allure.id('4_2')
@allure.epic('CartAddRemove')
@allure.feature('item_add_remove')
@allure.title('item add via item page and remove via cart page')
@pytest.mark.positive
def test_add_item_ip_2(browser, login, inv_page, item_page, cart_page):
    with allure.step('go to the item page'):
        inv_page.invent_imgs_find()[4].click()
    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.item_url_5, 'Wrong URL'
        assert item_page.item_name_find().text == ItemData.item5_name, 'Wrong name'
        assert item_page.item_img_find().get_attribute('src') == ItemData.item5_img, 'Wrong image'
        assert item_page.item_price_find().text == ItemData.item5_price, 'Wrong price'
    with allure.step('add the item to the cart'):
        item_page.item_add_find().click()
    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()
    with allure.step('check the current url and item name'):
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item5_name, 'Wrong name'
    with allure.step('remove the item from the cart'):
        cart_page.cart_remove_find().click()
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Wrong quantity'


@allure.id('4_3')
@allure.epic('CartAddRemove')
@allure.feature('item_add_remove')
@allure.title('item add and remove via inventory page')
@pytest.mark.positive
def test_add_item_mp(browser, login, inv_page, item_page, cart_page):
    with allure.step('add the item to the cart'):
        inv_page.invent_adds_find()[0].click()
    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.invent_names_find()[0].text == ItemData.item1_name, 'Wrong name'
        assert inv_page.invent_imgs_find()[0].get_attribute('src') == ItemData.item1_img, 'Wrong image'
        assert inv_page.invent_prices_find()[0].text == ItemData.item1_price, 'Wrong price'
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'
    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()
    with allure.step('check the current url and item name'):
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    with allure.step('go back to the inventory page with "CONTINUE SHOPPING" button'):
        cart_page.cart_return().click()
    with allure.step('remove the item from the cart'):
        inv_page.invent_removes_find()[0].click()
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Wrong quantity'

