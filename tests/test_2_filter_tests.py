import pytest
import allure

from pages.auth_page import login


@allure.id('2_1')
@allure.epic('InventoryFilter')
@allure.feature('filter')
@allure.title('name z-a filtration')
@pytest.mark.positive
def test_za_filter(browser, login, inv_page, filter_page):
    with allure.step('sort the items by name in descending order before the filtration'):
        items_first_za = inv_page.invent_names_find()
        za_first = []
        for item in items_first_za:
            za_first.append(item.text)
        za_first.sort(reverse=True)
        print(f'\n{za_first}')

    with allure.step('click the Name(Z to A) option'):
        filter_page.za_opt().click()

    with allure.step('check if the filter works properly'):
        items_then_za = inv_page.invent_names_find()
        za_then = []
        for item in items_then_za:
            za_then.append(item.text)
        print(f'\n{za_then}')

        assert za_first == za_then, 'The filter is broken'
    inv_page.refresh()


@allure.id('2_2')
@allure.epic('InventoryFilter')
@allure.feature('filter')
@allure.title('name a-z filtration')
@pytest.mark.positive
def test_az_filter(browser, login, inv_page, filter_page):
    with allure.step('sort the items by name in ascending order before the filtration'):
        items_first_az = inv_page.invent_names_find()
        az_first = []
        for item in items_first_az:
            az_first.append(item.text)
        az_first.sort(reverse=False)
        print(f'\n{az_first}')

    with allure.step('click the Name(A to Z) option'):
        filter_page.az_opt().click()

    with allure.step('check if the filter works properly'):
        items_then_az = inv_page.invent_names_find()
        az_then = []
        for item in items_then_az:
            az_then.append(item.text)
        print(f'\n{az_then}')

        assert az_first == az_then, 'The filter is broken'
    inv_page.refresh()


@allure.id('2_3')
@allure.epic('InventoryFilter')
@allure.feature('filter')
@allure.title('price low-high filtration')
@pytest.mark.positive
def test_lohi_filter(browser, login, inv_page, filter_page):
    with allure.step('sort the items by price in ascending order before the filtration'):
        items_first_lohi = inv_page.invent_prices_find()
        lohi_first = []
        for item in items_first_lohi:
            lohi_first.append(float(item.text.lstrip('$')))
        lohi_first.sort(reverse=False)
        print(f'\n{lohi_first}')

    with allure.step('click the Price(low to high) option'):
        filter_page.lohi_opt().click()

    with allure.step('check if the filter works properly'):
        items_then_lohi = inv_page.invent_prices_find()
        lohi_then = []
        for item in items_then_lohi:
            lohi_then.append(float(item.text.lstrip('$')))
        print(f'\n{lohi_then}')

        assert lohi_first == lohi_then, 'The filter is broken'
    inv_page.refresh()


@allure.id('2_4')
@allure.epic('InventoryFilter')
@allure.feature('filter')
@allure.title('price high-low filtration')
@pytest.mark.positive
def test_hilo_filter(browser, login, inv_page, filter_page):
    with allure.step('sort the items by price in descending order before the filtration'):
        items_first_hilo = inv_page.invent_prices_find()
        hilo_first = []
        for item in items_first_hilo:
            hilo_first.append(float(item.text.lstrip('$')))
        hilo_first.sort(reverse=True)
        print(f'\n{hilo_first}')

    with allure.step('click the Price(high to low) option'):
        filter_page.hilo_opt().click()

    with allure.step('check if the filter works properly'):
        items_then_hilo = inv_page.invent_prices_find()
        hilo_then = []
        for item in items_then_hilo:
            hilo_then.append(float(item.text.lstrip('$')))
        print(f'\n{hilo_then}')

        assert hilo_first == hilo_then, 'The filter is broken'
    inv_page.refresh()