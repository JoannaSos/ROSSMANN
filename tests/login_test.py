from tests.base_test import BaseTest
from pages.login_page import LoginPage
from data.login_test_data import *
from data.expected_result import Results
from utils.urls import Urls


class LoginTest(BaseTest):
    """Testy logowania się"""
    credentials_file_name = '../test_data/login_data.xlsx'

    def setUp(self):
        super().setUp()
        self.credentials = Credentials(self.credentials_file_name)
        self.login_page = LoginPage(self.driver)
        self.url = Urls.LOGIN_URL
        self.driver.get(self.url)

    def test_log_in_with_valid_credentials(self):
        self.login_page.accept_private_policy()
        self.login_page.enter_login(self.credentials.valid.username)
        self.login_page.enter_password(self.credentials.valid.password)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.check_if_user_is_logged_in())

    def test_login_with_not_existing_login(self):
        self.login_page.accept_private_policy()
        self.login_page.enter_login(self.credentials.notExistingLogin.username)
        self.login_page.enter_password(self.credentials.notExistingLogin.password)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.check_if_got_expected_feedback(Results.not_existing_login))

    def test_log_in_with_too_long_invalid_password(self):
        self.login_page.accept_private_policy()
        self.login_page.enter_login(self.credentials.tooLongLogin.username)
        self.login_page.enter_password(self.credentials.tooLongLogin.password)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.check_if_got_expected_feedback(Results.too_long_login))

    def test_log_in_with_empty_login(self):
        self.login_page.accept_private_policy()
        self.login_page.enter_login(self.credentials.emptyLogin.username)
        self.login_page.enter_password(self.credentials.emptyLogin.password)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.check_if_got_expected_feedback(Results.empty_login))

    def test_empty_login_and_password(self):
        self.login_page.accept_private_policy()
        self.login_page.enter_login(self.credentials.emptyLoginPassword.username)
        self.login_page.enter_password(self.credentials.emptyLoginPassword.password)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.check_if_got_expected_feedbacks(Results.empty_login, Results.empty_password))
