import pytest
from pages.auth_page import login
from locators.urls import URLs
from locators.order_locate import OrderData
from locators.item_locate import ItemData


# order one item with valid data
@pytest.mark.positive
def test_order_item_ok(browser, login, inv_page, cart_page, order_page):
    inv_page.invent_adds_find()[5].click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item6_name, 'Wrong name'
    assert cart_page.cart_item_descrs_find()[0].text == ItemData.item6_desc, 'Wrong description'
    assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item6_price.lstrip('$')), \
        'Wrong price'
    assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys(OrderData.fname_ok)
    order_page.order_lname().send_keys(OrderData.lname_ok)
    order_page.order_zip().send_keys(OrderData.zip_ok)

    order_page.order_continue().click()
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

    order_page.order_finish().click()
    assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
    assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
    assert cart_page.cart_badge_invisible(), 'Cart not empty'
    assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'


# order several items with invalid data
@pytest.mark.defect
@pytest.mark.negative
def test_order_items_wrong(browser, login, inv_page, cart_page, order_page):
    inv_page.invent_adds_find()[5].click()
    inv_page.invent_adds_find()[3].click()
    inv_page.invent_adds_find()[1].click()
    assert int(cart_page.cart_badge_visible().text) == 3, 'Wrong quantity'

    cart_page.cart_icon_find().click()
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

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys(OrderData.fname_wrong)
    order_page.order_lname().send_keys(OrderData.lname_wrong)
    order_page.order_zip().send_keys(OrderData.zip_wrong)

    order_page.order_continue().click()
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

    order_page.order_finish().click()
    assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
    assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
    assert cart_page.cart_badge_invisible(), 'Cart not empty'
    assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'


# order 0 items with empty order form
@pytest.mark.negative
@pytest.mark.defect
def test_order_empty(browser, login, inv_page, cart_page, order_page):
    assert cart_page.cart_badge_invisible(), 'Cart is full'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys('')
    order_page.order_lname().send_keys('')
    order_page.order_zip().send_keys('')

    order_page.order_continue().click()

    assert order_page.empty_order_form_error(), 'Ok'


# order 1 item with empty first name
@pytest.mark.negative
def test_order_empty_fname(browser, login, inv_page, cart_page, order_page):
    inv_page.invent_adds_find()[0].click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'


    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
    assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
    assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys('')
    order_page.order_lname().send_keys(OrderData.lname_ok)
    order_page.order_zip().send_keys(OrderData.zip_ok)

    order_page.order_continue().click()

    assert order_page.empty_order_form_error(), 'Ok'
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



# order 1 item with empty last name
@pytest.mark.negative
def test_order_empty_lname(browser, login, inv_page, cart_page, order_page):
    inv_page.invent_adds_find()[0].click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
    assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
    assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys(OrderData.fname_ok)
    order_page.order_lname().send_keys('')
    order_page.order_zip().send_keys(OrderData.zip_ok)

    order_page.order_continue().click()

    assert order_page.empty_order_lname_form_error(), 'Ok'
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



# order 1 item with empty zip
@pytest.mark.negative
def test_order_empty_zip(browser, login, inv_page, cart_page, order_page):
    inv_page.invent_adds_find()[0].click()
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'
    assert cart_page.cart_item_names_find()[0].text == ItemData.item1_name, 'Wrong name'
    assert cart_page.cart_item_descrs_find()[0].text == ItemData.item1_desc, 'Wrong description'
    assert float(cart_page.cart_item_prices_find()[0].text) == float(ItemData.item1_price.lstrip('$')), \
        'Wrong price'
    assert int(cart_page.cart_quantities_find()[0].text) == 1, 'Wrong item quantity'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys(OrderData.fname_ok)
    order_page.order_lname().send_keys(OrderData.lname_ok)
    order_page.order_zip().send_keys('')

    order_page.order_continue().click()

    assert order_page.empty_order_zip_form_error(), 'Ok'
    assert int(cart_page.cart_badge_visible().text) == 1, 'Wrong quantity'



# order 0 items with valid data
@pytest.mark.defect
@pytest.mark.negative
def test_order_empty_ok(browser, login, inv_page, cart_page, order_page):
    assert cart_page.cart_badge_invisible(), 'Cart is full'

    cart_page.cart_icon_find().click()
    assert browser.current_url == URLs.cart_url, 'Wrong URL'

    order_page.order_checkout().click()
    assert browser.current_url == URLs.checkout_url, 'Wrong URL'
    order_page.order_fname().send_keys(OrderData.fname_ok)
    order_page.order_lname().send_keys(OrderData.lname_ok)
    order_page.order_zip().send_keys(OrderData.zip_ok)

    order_page.order_continue().click()

    items_sum = int(order_page.subtotal().text.lstrip('Item total: $'))
    assert items_sum == 0, 'Wrong subtotal price'
    tax_summ = round(items_sum * OrderData.tax_rate, 2)
    assert tax_summ == float(order_page.tax().text.lstrip('Tax: $'))
    total_sum = float(order_page.total().text.lstrip('Total: $'))
    assert total_sum == items_sum + tax_summ, 'Wrong total price'

    order_page.order_finish().click()
    assert browser.current_url == URLs.complete_url and order_page.complete_thanks(), \
        'Wrong url, success message not provided'
    assert order_page.order_thanks_img().get_attribute('src') == OrderData.thanks_img, 'Wrong image'
    assert cart_page.cart_badge_invisible(), 'Cart not empty'
    assert len(cart_page.cart_items_cards()) == 0, f'{len(cart_page.cart_items_cards())} items in cart'

