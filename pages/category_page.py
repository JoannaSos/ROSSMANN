from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class Locators:
    PRICE_RANGE_LABEL = (By.XPATH, "//div[text()='Przedział cenowy']")
    ACCEPT_POLICY_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    PRICE_END_LABEL = (By.ID, "prize-end")
    PRICE_START_LABEL = (By.NAME, "statePriceFrom")
    SHOW_PRODUCTS_BUTTON = (By.CLASS_NAME, "btn-primary")
    EMPTY_PRODUCTS_BUTTON = (By.XPATH, "//button[contains(text(),'Brak produktów')]")
    TILE_PRODUCT = (By.CLASS_NAME, "tile-product")
    PROMO_PRICE_PRODUCT = (By.CLASS_NAME, "tile-product__promo-price")
    REGULAR_PRICE_PRODUCT = (By.CLASS_NAME, "tile-product__current-price")
    SHOW_PRODUCTS_NUMBER_DROP_DOWN_LIST = (By.XPATH,
                                           "//div[@class='sri-select no-border pointer']//div[contains(@class,'form-control sri-select__selected-item')]")
    SELECTED_NUMBER_OF_PRODUCTS = (By.XPATH, "//div[contains(@class, 'sri-select__item ')]")
    SEARCH = (By.CLASS_NAME, "show-search")
    SEARCH_TEXT = (By.XPATH, "/html/body/div[4]/div/div[1]/div/div/section/div[1]/div/div/input")
    SPAN = (By.TAG_NAME, "span")
    STRONG = (By.TAG_NAME, "strong")
    CHECKBOX = (By.XPATH, "//span[contains(text(),'XXXX')]")
    FILTERED_PRODUCT = (By.CLASS_NAME, "m-n1")
    SORTING = (By.XPATH, "//span[text()='Sortuj wg domyślnie']")
    DESC_SORTING_PRICE = (By.XPATH, "//div[contains(text(),'cena od najwyższej')]")
    ASC_SORTING_PRICE = (By.XPATH, "//div[contains(text(),'cena od najniższej')]")
    SORTING_A_Z_NAME = (By.XPATH, "//div[contains(text(),'nazwa a-z')]")
    SORTING_Z_A_NAME = (By.XPATH, "//div[contains(text(),'nazwa z-a')]")


class CategoryPage(BasePage):

    def accept_private_policy(self):
        self.click_when_element_is_clickable(Locators.ACCEPT_POLICY_BUTTON)

    def click_price_range_label(self):
        self.scroll_and_click_when_element_is_present(Locators.PRICE_RANGE_LABEL)

    def scroll_and_click_show_products(self):
        try:
            self.scroll_and_click_when_element_is_present(Locators.SHOW_PRODUCTS_BUTTON)
        except ElementClickInterceptedException:
            self.scroll_and_click_when_element_is_present(Locators.SHOW_PRODUCTS_BUTTON)

    def click_show_products(self):
        try:
            self.driver.find_element(*Locators.SHOW_PRODUCTS_BUTTON).click()
        except ElementClickInterceptedException:
            self.driver.find_element(*Locators.SHOW_PRODUCTS_BUTTON).click()

    def click_show_products_number(self, products_per_page):
        show_number_of_products = self.driver.find_element(*Locators.SHOW_PRODUCTS_NUMBER_DROP_DOWN_LIST)
        show_number_of_products.click()
        show_number_of_products = self.driver.find_element(*Locators.SHOW_PRODUCTS_NUMBER_DROP_DOWN_LIST)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(show_number_of_products)
        action.perform()
        selected_list_number_of_products = show_number_of_products.find_elements(*Locators.SELECTED_NUMBER_OF_PRODUCTS)
        for number_of_products_option in selected_list_number_of_products:
            number_of_products = int(number_of_products_option.text.split(" ")[0])
            if number_of_products == products_per_page:
                number_of_products_option.click()

    def click_search_product_input(self):
        self.driver.find_element(*Locators.SEARCH).click()
        self.click_when_element_is_clickable(Locators.SEARCH_TEXT)

    def click_checkbox(self, brand):
        Locators.CHECKBOX = (Locators.CHECKBOX[0], Locators.CHECKBOX[1].replace("XXXX", brand))
        element = self.driver.find_element(*Locators.CHECKBOX)
        self.driver.execute_script("arguments[0].click();", element)
        Locators.CHECKBOX = (Locators.CHECKBOX[0], Locators.CHECKBOX[1].replace(brand, "XXXX"))

    def click_sorting_by_desc_price(self):
        self.click_when_element_is_clickable(Locators.SORTING)
        self.click_when_element_is_clickable(Locators.DESC_SORTING_PRICE)

    def click_sorting_by_asc_price(self):
        self.driver.find_element(*Locators.SORTING).click()
        self.click_when_element_is_clickable(Locators.ASC_SORTING_PRICE)

    def click_sorting_by_a_z_name(self):
        self.driver.find_element(*Locators.SORTING).click()
        self.click_when_element_is_clickable(Locators.SORTING_A_Z_NAME)

    def click_sorting_by_z_a_name(self):
        self.driver.find_element(*Locators.SORTING).click()
        self.click_when_element_is_clickable(Locators.SORTING_Z_A_NAME)

    def check_products_filtered_by_min_and_max_price(self, min_price, max_price):
        products = self.find_products()
        for product in products:
            price = self.find_price(product)
            if price > max_price or price < min_price:
                return False
        return True

    def check_products_filtered_by_max_price(self, max_price):
        products = self.find_products()
        for product in products:
            price = self.find_price(product)
            if price > max_price:
                return False
        return True

    def check_if_product_contains_searching_text(self, searching_text):
        products = self.find_products()
        for product in products:
            span = product.find_element(*Locators.SPAN)
            if searching_text not in span.text:
                return False
        return True

    def check_if_product_contains_searching_brand(self, searching_text):
        products = self.find_products()
        for product in products:
            strong = product.find_element(*Locators.STRONG)
            if searching_text not in strong.text:
                return False
        return True

    def check_if_products_sorted_by_desc_price(self):
        products = self.find_products()
        for product_index in range(0, len(products) - 1):
            current_item_price = self.find_price(products[product_index])
            next_item_price = self.find_price(products[product_index + 1])
            if current_item_price < next_item_price:
                return False
        return True

    def check_if_products_sorted_by_asc_price(self):
        products = self.find_products()
        for product_index in range(0, len(products) - 1):
            current_item_price = self.find_price(products[product_index])
            next_item_price = self.find_price(products[product_index + 1])
            if current_item_price > next_item_price:
                return False
        return True

    def check_sorting_products_by_name_a_z(self):
        products = self.find_products()
        for product_index in range(0, len(products) - 1):
            current_item_name = self.find_name(products[product_index])
            next_item_name = self.find_name(products[product_index + 1])
            if current_item_name > next_item_name:
                return False
        return True

    def check_sorting_products_by_name_z_a(self):
        products = self.find_products()
        for product_index in range(0, len(products) - 1):
            current_item_name = self.find_name(products[product_index])
            next_item_name = self.find_name(products[product_index + 1])
            if current_item_name < next_item_name:
                return False
        return True

    def enter_max_price(self, max_price):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Locators.PRICE_END_LABEL))
        self.driver.find_element(*Locators.PRICE_END_LABEL).send_keys(max_price)

    def enter_min_price(self, min_price):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Locators.PRICE_START_LABEL))
        self.driver.find_element(*Locators.PRICE_START_LABEL).send_keys(min_price)

    def enter_searching_product(self, searching_product):
        self.driver.find_element(*Locators.SEARCH_TEXT).send_keys(searching_product)
        self.driver.find_element(*Locators.SEARCH_TEXT).send_keys(Keys.ENTER)

    def find_products(self):
        try:
            button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.EMPTY_PRODUCTS_BUTTON))
        except:
            button = None
        products = []

        if button is None:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.TILE_PRODUCT))
            products = self.driver.find_elements(*Locators.TILE_PRODUCT)

        return products

    def find_price(self, product):
        try:
            price_str = self.get_text_when_element_present(Locators.REGULAR_PRICE_PRODUCT)
        except:
            price_str = self.get_text_when_element_present(Locators.PROMO_PRICE_PRODUCT)
        price = float(price_str[:-3].replace(",", "."))
        return price

    def find_name(self, product):
        name = product.find_element(*Locators.STRONG).text
        return name

    def scroll_to_brand_label(self):
        self.scroll_to_element_when_is_present(Locators.FILTERED_PRODUCT)
