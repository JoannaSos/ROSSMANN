from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import Urls


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.url = Urls.BASE_URL

    def click_when_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elem = wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def scroll_and_click_when_element_is_present(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elem = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def scroll_to_element_when_is_present(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    def get_text_when_element_present(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)).text

    def get_current_url(self):
        return self.driver.current_url
