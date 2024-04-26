import pytest
import requests
import allure

from pages.auth_page import login_logout, login_glitch, login_problem, login_wrong
from locators.auth_locate import AuthLocate, AuthData
from locators.urls import URLs


@allure.id('1_1')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('standard user authorization')
@pytest.mark.positive
def test_login_standard(browser, login, inv_page):
    with allure.step('check the current url, the inventory page header and the presence of the goods on the page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.invent_header().text == 'Products', 'Wrong header'
        assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nStandard user...')


@allure.id('1_2')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('locked out user authorization')
@pytest.mark.positive
def test_login_lockedout(browser, login_logout, log_page):
    with allure.step('check the current url and the presence of the error'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.logout_err() == AuthData.error_text_4, 'Login success'

    print(f'\nlocked out... {log_page.logout_err()}')


@allure.id('1_3')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('problem user authorization')
@pytest.mark.positive
def test_login_problem(browser, login_problem, inv_page):
    with allure.step('check the current url, the inventory page header and the presence of the goods on the page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.invent_header().text == 'Products', 'Wrong header'
        assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nProblem user...')

    with allure.step('check if there are broken images on the page and collect them'):
        imgs = inv_page.invent_imgs_find()
        broken_url_img = 'WithGarbageOnItToBreakTheUrl'

        for img in imgs:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    assert response.status_code == 404, 'Image Not Found'
                    assert broken_url_img in img.get_dom_attribute('src'), 'Image Not Visible'
                    print(f'\n{response} Image: {img.get_dom_attribute("src")} is not visible')


@allure.id('1_4')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('glitched user authorization')
@pytest.mark.positive
def test_login_glitch(browser, login_glitch, inv_page):
    with allure.step('check the current url, the inventory page header and the presence of the goods on the page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.invent_header().text == 'Products', 'Wrong header'
        assert len(inv_page.invent_cards_find()) > 0, 'No goods found'

    print(f'\nGlitch user...')


@allure.id('1_5')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('authorization with wrong data')
@pytest.mark.negative
def test_login_wrong(browser, log_page, login_wrong):
    with allure.step('check the current url and the presence of the error'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.wrong_err() == AuthData.error_text_1, 'Login success'

    print(f'\nWrong login... {log_page.wrong_err()}')


@allure.id('1_6')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('authorization with empty form')
@pytest.mark.negative
def test_login_empty(browser, log_page):

    log_page.open()
    with allure.step('log in with empty form'):
        log_page.name_field().send_keys('')
        log_page.pass_field().send_keys('')
        log_page.btn_login().click()

    with allure.step('check the current url and the presence of the error'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.empty_err() == AuthData.error_text_2, 'Login success'

    print(f'\nEmpty login... {log_page.empty_err()}')


@allure.id('1_7')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('authorization with empty username')
@pytest.mark.negative
def test_login_empty_name(browser, log_page):

    log_page.open()
    with allure.step('log in with the empty username'):
        log_page.name_field().send_keys('')
        log_page.pass_field().send_keys(AuthData.password_ok)
        log_page.btn_login().click()

    with allure.step('check the current url and the presence of the error'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.empty_err() == AuthData.error_text_2, 'Login success'

    print(f'\nWrong login... {log_page.empty_err()}')


@allure.id('1_8')
@allure.epic('AuthorizationPage')
@allure.feature('auth')
@allure.title('authorization with empty password')
@pytest.mark.negative
def test_login_empty_pass(browser, log_page):

    log_page.open()
    with allure.step('log in with the empty password'):
        log_page.name_field().send_keys(AuthData.username_ok)
        log_page.pass_field().send_keys('')
        log_page.btn_login().click()

    with allure.step('check the current url and the presence of the error'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.empty_pass_err() == AuthData.error_text_3, 'Login success'

    print(f'\nWrong login... {log_page.empty_pass_err()}')

