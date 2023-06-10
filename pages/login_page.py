from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from utils.urls import Urls
from pages.base_page import BasePage



class Locators:
    """Lokatory strony logowania"""
    USERNAME_INPUT = (By.ID, "login-user")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOG_OUT_BUTTON = (By.XPATH, '//button[contains(text(),"Wyloguj")]')
    ACCEPT_POLICY_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    PROFILE_BUTTON = (By.LINK_TEXT, "Profil")
    INVALID_FEEDBACK = (By.CLASS_NAME, "invalid-feedback")


class LoginPage(BasePage):
    """Strona logowania"""

    def accept_private_policy(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Locators.ACCEPT_POLICY_BUTTON)).click()

    def enter_login(self, username):
        self.driver.find_element(*Locators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.scroll_and_click_when_element_is_present(Locators.LOGIN_BUTTON)

    def move_cursor_to_profile_button(self):
        action = webdriver.ActionChains(self.driver)
        profile_button = self.driver.find_element(*Locators.PROFILE_BUTTON)
        action.move_to_element(profile_button)
        action.perform()

    def check_if_user_is_logged_in(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(Urls.BASE_URL))
        self.move_cursor_to_profile_button()
        log_out_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(Locators.LOG_OUT_BUTTON))
        if log_out_button is None:
            return False
        return True

    def check_if_got_expected_feedback(self, expected_result):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.INVALID_FEEDBACK))
        invalid_feeback_div = self.driver.find_element(*Locators.INVALID_FEEDBACK)
        if invalid_feeback_div.text == expected_result:
            return True
        return False

    def check_if_got_expected_feedbacks(self, login_expected_result, password_expected_result):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.INVALID_FEEDBACK))
        invalid_feebacks = self.driver.find_elements(*Locators.INVALID_FEEDBACK)
        if invalid_feebacks[0].text == login_expected_result and invalid_feebacks[1].text == password_expected_result:
            return True
        return False
