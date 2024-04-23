import pytest
# import requests

from pages.auth_page import login_logout, login_glitch, login_problem
from locators.auth_locate import AuthLocate, AuthData
from locators.urls import URLs


# login for standard_user
@pytest.mark.positive
def test_login_standard(browser, login, inv_page):
    assert browser.current_url == URLs.inventory_url, 'Wrong URL'
    assert inv_page.invent_header().text == 'Products', 'Wrong header'
    assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nStandard user...')


# login for locked_out_user
@pytest.mark.positive
def test_login_lockedout(browser, login_logout, log_page):
    assert browser.current_url == URLs.auth_url, 'Wrong URL'
    assert log_page.logout_err() == AuthData.error_text_4, 'Login success'

    print(f'\nlocked out... {log_page.logout_err()}')


# login for problem_user
@pytest.mark.positive
def test_login_problem(browser, login_problem, inv_page):
    assert browser.current_url == URLs.inventory_url, 'Wrong URL'
    assert inv_page.invent_header().text == 'Products', 'Wrong header'
    assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nProblem user...')


# login for glitch_user
@pytest.mark.positive
def test_login_problem(browser, login_glitch, inv_page):
    assert browser.current_url == URLs.inventory_url, 'Wrong URL'
    assert inv_page.invent_header().text == 'Products', 'Wrong header'
    assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nGlitch user...')


# login with wrong data
@pytest.mark.negative
def test_login_wrong(browser, log_page):

    log_page.open()
    log_page.name_field().send_keys(AuthData.username_wrong)
    log_page.pass_field().send_keys(AuthData.password_wrong)
    log_page.btn_login().click()

    assert browser.current_url == URLs.auth_url, 'Wrong URL'
    assert log_page.wrong_err() == AuthData.error_text_1, 'Login success'

    print(f'\nWrong login... {log_page.wrong_err()}')


# # login with empty fields
# @pytest.mark.negative
# def test_login_wrong(browser, log_page):
#
#     log_page.open()
#     log_page.name_field().send_keys('')
#     log_page.pass_field().send_keys('')
#     log_page.btn_login().click()
#
#     assert browser.current_url == URLs.auth_url, 'Wrong URL'
#     assert log_page.empty_err() == AuthData.error_text_2, 'Login success'
#
#     print(f'\nWrong login... {log_page.empty_err()}')

