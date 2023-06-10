import unittest
from utils.urls import Urls
from selenium import webdriver
from pages.base_page import BasePage


class BaseTest(unittest.TestCase):
    def setUp(self):
        """Warunki wstępne każdego testu"""
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.url = Urls.BASE_URL
        self.driver.get(self.url)
        self.base_page = BasePage(self.driver)

    def test_verify_page(self):
        self.assertTrue(self.url, self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
