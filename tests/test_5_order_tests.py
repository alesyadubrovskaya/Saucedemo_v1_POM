import pytest
import allure
from pages.auth_page import login
from locators.urls import URLs
from locators.order_locate import OrderData
from locators.item_locate import ItemData


@allure.id('5_1')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 1 item with valid data')
@pytest.mark.positive
def test_order_item_ok(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the item to the cart'):
        inv_page.invent_adds_find()[5].click()

    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item6_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item6_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item6_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form with valid data'):
        order_page.order_fname().send_keys(OrderData.fname_ok)
        order_page.order_lname().send_keys(OrderData.lname_ok)
        order_page.order_zip().send_keys(OrderData.zip_ok)

    with allure.step('go to the order info page'):
        order_page.order_continue().click()

    with allure.step('check the current url and order info'):
        assert browser.current_url == URLs.confirm_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item6_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item6_desc, 'Wrong description'
        assert cart_page.cart_item_prices_find()[0].text == ItemData.item6_price, 'Wrong price'
        assert int(order_page.order_item_quants()[0].text) == 1, 'Wrong item quantity'

        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == float(ItemData.item6_price.lstrip('$'))
        tax_summ = round(items_sum * OrderData.tax_rate, 2)
        assert tax_summ == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == items_sum + tax_summ, 'Wrong total price'

    with allure.step('go to the confirmation page'):
        order_page.order_finish().click()

    with allure.step('check the current url and page info'):
        assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
        assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
        assert cart_page.cart_badge_invisible(), 'Cart not empty'
        assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'


@allure.id('5_2')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order several items with invalid data')
@pytest.mark.defect
@pytest.mark.negative
def test_order_items_wrong(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the items to the cart'):
        inv_page.invent_adds_find()[5].click()
        inv_page.invent_adds_find()[3].click()
        inv_page.invent_adds_find()[1].click()

    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 3, 'Wrong quantity'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url and items info'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item6_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item6_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item6_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names_find()[1].text == ItemData.item4_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[1].text == ItemData.item4_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[1].text) == float(ItemData.item4_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[1].text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names_find()[2].text == ItemData.item2_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[2].text == ItemData.item2_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[2].text) == float(ItemData.item2_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[2].text) == 1, 'Wrong item quantity'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form with invalid data'):
        order_page.order_fname().send_keys(OrderData.fname_wrong)
        order_page.order_lname().send_keys(OrderData.lname_wrong)
        order_page.order_zip().send_keys(OrderData.zip_wrong)

    with allure.step('go to the order info page'):
        order_page.order_continue().click()

    with allure.step('check the current url and order info'):
        assert browser.current_url == URLs.confirm_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item6_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item6_desc, 'Wrong description'
        assert cart_page.cart_item_prices_find()[0].text == ItemData.item6_price, 'Wrong price'
        assert int(order_page.order_item_quants()[0].text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names_find()[1].text == ItemData.item4_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[1].text == ItemData.item4_desc, 'Wrong description'
        assert cart_page.cart_item_prices_find()[1].text == ItemData.item4_price, 'Wrong price'
        assert int(order_page.order_item_quants()[1].text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names_find()[2].text == ItemData.item2_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[2].text == ItemData.item2_desc, 'Wrong description'
        assert cart_page.cart_item_prices_find()[2].text == ItemData.item2_price, 'Wrong price'
        assert int(order_page.order_item_quants()[2].text) == 1, 'Wrong item quantity'

        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == float(ItemData.item6_price.lstrip('$')) + float(ItemData.item4_price.lstrip('$')) + \
           float(ItemData.item2_price.lstrip('$')), 'Wrong subtotal price'
        tax_summ = round(items_sum * OrderData.tax_rate, 2)
        assert tax_summ == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == items_sum + tax_summ, 'Wrong total price'

    with allure.step('go to the confirmation page'):
        order_page.order_finish().click()

    with allure.step('check the current url and page info'):
        assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
        assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
        assert cart_page.cart_badge_invisible(), 'Cart not empty'
        assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'


@allure.id('5_3')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 0 items with empty form')
@pytest.mark.negative
@pytest.mark.defect
def test_order_empty(browser, login, inv_page, cart_page, order_page):
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Cart is full'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('leave the customer form empty'):
        order_page.order_fname().send_keys('')
        order_page.order_lname().send_keys('')
        order_page.order_zip().send_keys('')

    with allure.step('go to the confirmation page'):
        order_page.order_continue().click()

    with allure.step('check if there is an error'):
        assert order_page.empty_order_form_error(), 'Ok'


@allure.id('5_4')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 1 item with empty first name')
@pytest.mark.negative
def test_order_empty_fname(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the item to the cart'):
        inv_page.invent_adds_find()[0].click()

    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form empty leaving the first name field empty'):
        order_page.order_fname().send_keys('')
        order_page.order_lname().send_keys(OrderData.lname_ok)
        order_page.order_zip().send_keys(OrderData.zip_ok)

    with allure.step('go to the confirmation page'):
        order_page.order_continue().click()

    with allure.step('check if there is an error and the presence of the cart icon with the amount of goods'):
        assert order_page.empty_order_form_error(), 'Ok'
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



@allure.id('5_5')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 1 item with empty last name')
@pytest.mark.negative
def test_order_empty_lname(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the item to the cart'):
        inv_page.invent_adds_find()[0].click()

    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form empty leaving the last name field empty'):
        order_page.order_fname().send_keys(OrderData.fname_ok)
        order_page.order_lname().send_keys('')
        order_page.order_zip().send_keys(OrderData.zip_ok)

    with allure.step('go to the confirmation page'):
        order_page.order_continue().click()

    with allure.step('check if there is an error and the presence of the cart icon with the amount of goods'):
        assert order_page.empty_order_lname_form_error(), 'Ok'
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



@allure.id('5_6')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 1 item with empty zip')
@pytest.mark.negative
def test_order_empty_zip(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the item to the cart'):
        inv_page.invent_adds_find()[0].click()

    with allure.step('check the presence of the icon with quantity of goods in cart'):
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url and item info'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
        assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
        assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
        assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form empty leaving the zip field empty'):
        order_page.order_fname().send_keys(OrderData.fname_ok)
        order_page.order_lname().send_keys(OrderData.lname_ok)
        order_page.order_zip().send_keys('')

    with allure.step('go to the confirmation page'):
        order_page.order_continue().click()

    with allure.step('check if there is an error and the presence of the cart icon with the amount of goods'):
        assert order_page.empty_order_zip_form_error(), 'Ok'
        assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



@allure.id('5_7')
@allure.epic('OrderModule')
@allure.feature('order')
@allure.title('order 0 items with valid data')
@pytest.mark.defect
@pytest.mark.negative
def test_order_empty_ok(browser, login, inv_page, cart_page, order_page):
    with allure.step('check if the icon with quantity of goods in cart is gone'):
        assert cart_page.cart_badge_invisible(), 'Cart is full'

    with allure.step('go to the cart page'):
        cart_page.cart_icon_find().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.cart_url, 'Wrong URL'

    with allure.step('go to the checkout page'):
        order_page.order_checkout().click()

    with allure.step('check the current url'):
        assert browser.current_url == URLs.checkout_url, 'Wrong URL'

    with allure.step('fill the customer form with valid data'):
        order_page.order_fname().send_keys(OrderData.fname_ok)
        order_page.order_lname().send_keys(OrderData.lname_ok)
        order_page.order_zip().send_keys(OrderData.zip_ok)

    with allure.step('go to the order info page'):
        order_page.order_continue().click()

        items_sum = int(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == 0, 'Wrong subtotal price'
        tax_summ = round(items_sum * OrderData.tax_rate, 2)
        assert tax_summ == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == items_sum + tax_summ, 'Wrong total price'

    with allure.step('go to the confirmation page'):
        order_page.order_finish().click()

    with allure.step('check the current url and order info'):
        assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
        assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
        assert cart_page.cart_badge_invisible(), 'Cart not empty'
        assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'

