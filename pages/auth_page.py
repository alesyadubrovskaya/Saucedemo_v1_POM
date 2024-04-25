import pytest
from pages.base_page import BasePage
from locators.auth_locate import AuthLocate, AuthData


@pytest.fixture()
def login(log_page):
    log_page.auth(AuthData.username_ok, AuthData.password_ok)


@pytest.fixture()
def login_logout(log_page):
    log_page.auth(AuthData.username_logout, AuthData.password_ok)


@pytest.fixture()
def login_problem(log_page):
    log_page.auth(AuthData.username_problem, AuthData.password_ok)


@pytest.fixture()
def login_glitch(log_page):
    log_page.auth(AuthData.username_glitch, AuthData.password_ok)


@pytest.fixture()
def login_wrong(log_page):
    log_page.auth(AuthData.username_wrong, AuthData.password_wrong)


class AuthPage(BasePage):
    def name_field(self):
        return self.is_visible(AuthLocate.username_field)

    def name_input(self, username):
        return self.is_visible(AuthLocate.username_field).send_keys(username)

    def pass_field(self):
        return self.is_visible(AuthLocate.password_field)

    def pass_input(self, password):
        return self.is_visible(AuthLocate.password_field).send_keys(password)

    def btn_login(self):
        return self.is_clickable(AuthLocate.login_button)

    def press_login(self):
        return self.is_clickable(AuthLocate.login_button).click()

    def auth(self, username, password):
        self.open()
        self.name_input(username)
        self.pass_input(password)
        self.press_login()
        return self

    @staticmethod
    def logout_err():
        return AuthData.error_text_4

    @staticmethod
    def wrong_err():
        return AuthData.error_text_1

    @staticmethod
    def empty_err():
        return AuthData.error_text_2

    @staticmethod
    def empty_pass_err():
        return AuthData.error_text_3
