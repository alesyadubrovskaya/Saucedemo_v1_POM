import pytest

from pages.auth_page import login


# testing of the za filter
@pytest.mark.positive
def test_za_filter(browser, login, inv_page, filter_page):
    # the goods before the za filter is chosen
    items_first_za = inv_page.invent_names_find()
    za_first = []
    for item in items_first_za:
        za_first.append(item.text)
    za_first.sort(reverse=True)
    print(f'\n{za_first}')

    filter_page.za_opt().click()

    # the goods after the za filter is chosen
    items_then_za = inv_page.invent_names_find()
    za_then = []
    for item in items_then_za:
        za_then.append(item.text)
    print(f'\n{za_then}')

    assert za_first == za_then, 'The filter is broken'
    inv_page.refresh()


# testing of the az filter
@pytest.mark.positive
def test_az_filter(browser, login, inv_page, filter_page):
    # the goods before the az filter is chosen
    items_first_az = inv_page.invent_names_find()
    az_first = []
    for item in items_first_az:
        az_first.append(item.text)
    az_first.sort(reverse=False)
    print(f'\n{az_first}')

    filter_page.az_opt().click()

    # the goods after the az filter is chosen
    items_then_az = inv_page.invent_names_find()
    az_then = []
    for item in items_then_az:
        az_then.append(item.text)
    print(f'\n{az_then}')

    assert az_first == az_then, 'The filter is broken'
    inv_page.refresh()


# testing of the low-high filter
@pytest.mark.positive
def test_lohi_filter(browser, login, inv_page, filter_page):
    # the goods before the low-high filter is chosen
    items_first_lohi = inv_page.invent_prices_find()
    lohi_first = []
    for item in items_first_lohi:
        lohi_first.append(float(item.text.lstrip('$')))
    lohi_first.sort(reverse=False)
    print(f'\n{lohi_first}')

    filter_page.lohi_opt().click()

    # the goods after the low-high filter is chosen
    items_then_lohi = inv_page.invent_prices_find()
    lohi_then = []
    for item in items_then_lohi:
        lohi_then.append(float(item.text.lstrip('$')))
    print(f'\n{lohi_then}')

    assert lohi_first == lohi_then, 'The filter is broken'
    inv_page.refresh()


# testing of the high-low filter
@pytest.mark.positive
def test_hilo_filter(browser, login, inv_page, filter_page):
    # the goods before the high-low filter is chosen
    items_first_hilo = inv_page.invent_prices_find()
    hilo_first = []
    for item in items_first_hilo:
        hilo_first.append(float(item.text.lstrip('$')))
    hilo_first.sort(reverse=True)
    print(f'\n{hilo_first}')

    filter_page.hilo_opt().click()

    # the goods after the high-low filter is chosen
    items_then_hilo = inv_page.invent_prices_find()
    hilo_then = []
    for item in items_then_hilo:
        hilo_then.append(float(item.text.lstrip('$')))
    print(f'\n{hilo_then}')

    assert hilo_first == hilo_then, 'The filter is broken'
    inv_page.refresh()