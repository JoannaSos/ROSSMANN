from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Locators:
    ACCEPT_POLICY_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    E_MAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    CHECKBOX_REGULATION = (By.XPATH, '//small[contains(text(),"Oświadczam, że")]')
    CHECKBOX_NEWSLETTER = (By.XPATH, '//small[contains(text(),"Tak, chcę otrzymywać newsletter Rossmanna! Zapozna")]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@type="submit"]')
    INVALID_FEEDBACK_CAPTCHA = (By.XPATH, "//div[text()='Nieprawidłowa CAPTCHa']")
    INVALID_FEEDBACK_TOO_SHORT_AND_TO0_LONG_PASSWORD = (
        By.XPATH, "//div[contains(text(),'Hasło musi zawierać od 8 do 64 znaków.')]")


class RegistrationPage(BasePage):

    def accept_private_policy(self):

        self.click_when_element_is_clickable(Locators.ACCEPT_POLICY_BUTTON)

    def accept_regulation(self):
        checkbox_regulation = self.driver.find_element(*Locators.CHECKBOX_REGULATION)
        checkbox_regulation.click()

    def accept_newsletter(self):
        checkbox_newsletter = self.driver.find_element(*Locators.CHECKBOX_NEWSLETTER)
        self.driver.execute_script("arguments[0].click();", checkbox_newsletter)

    def enter_email(self, email):
        self.driver.find_element(*Locators.E_MAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_registration_button(self):
        wait = WebDriverWait(self.driver, 20)
        elem = wait.until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON))
        self.driver.execute_script("arguments[0].click();", elem)

    def check_if_got_expected_feedback(self, expected_result):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.INVALID_FEEDBACK_TOO_SHORT_AND_TO0_LONG_PASSWORD))
        invalid_feedback_div = self.driver.find_element(*Locators.INVALID_FEEDBACK_TOO_SHORT_AND_TO0_LONG_PASSWORD)
        if invalid_feedback_div.text == expected_result:
            return True
        return False

    def check_if_got_invalid_captcha(self, expected_result):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.INVALID_FEEDBACK_CAPTCHA))
        invalid_feedback_div = self.driver.find_element(*Locators.INVALID_FEEDBACK_CAPTCHA)
        if invalid_feedback_div.text == expected_result:
            return True
        return False
