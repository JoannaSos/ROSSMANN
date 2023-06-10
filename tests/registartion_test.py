from faker import Faker
from tests.base_test import BaseTest
from pages.registartion_page import RegistrationPage
from data.expected_result import Results
from utils.urls import Urls


class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.registration_page = RegistrationPage(self.driver)
        self.url = Urls.REGISTRATION_URL
        self.driver.get(self.url)
        self.faker = Faker()

    def test_registration_in_without_captcha(self):
        email = self.faker.email()
        password = self.faker.password()
        self.registration_page.accept_private_policy()
        self.registration_page.enter_email(email)
        self.registration_page.enter_password(password)
        self.registration_page.accept_regulation()
        self.registration_page.accept_newsletter()
        self.registration_page.click_registration_button()
        self.assertTrue(self.registration_page.check_if_got_invalid_captcha(Results.missing_captcha))

    def test_log_in_with_invalid_password(self):
        email = self.faker.email()
        password = self.faker.password()[0:3]
        self.registration_page.accept_private_policy()
        self.registration_page.enter_email(email)
        self.registration_page.enter_password(password)
        self.registration_page.accept_regulation()
        self.registration_page.accept_newsletter()
        self.registration_page.click_registration_button()
        self.assertTrue(self.registration_page.check_if_got_expected_feedback(Results.too_short_password_status))
