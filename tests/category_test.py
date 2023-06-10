from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from pages.category_page import CategoryPage
from utils.urls import Urls
import time


@ddt
class CategoryTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.category_page = CategoryPage(self.driver)
        self.url = Urls.CATEGORY_FACE_URL
        self.driver.get(self.url)

    @data(24, 48, 96)
    def test_changing_number_of_products_on_the_page(self, products_per_page):
        self.category_page.accept_private_policy()
        self.category_page.click_show_products_number(products_per_page)
        time.sleep(5)
        products = self.category_page.find_products()
        self.assertLessEqual(products_per_page, len(products))

    @data(4, 8, 15, 20, 40)
    def test_filtering_by_max_price(self, max_price):
        self.category_page.accept_private_policy()
        self.category_page.click_price_range_label()
        self.category_page.enter_max_price(max_price)
        self.category_page.click_show_products()
        self.assertTrue(self.category_page.check_products_filtered_by_max_price(max_price))

    @data((3, 10), (8, 15), (20, 35), (34, 80))
    @unpack
    def test_filtering_by_min_and_max_price(self, min_price, max_price):
        self.category_page.accept_private_policy()
        self.category_page.click_price_range_label()
        self.category_page.enter_min_price(min_price)
        self.category_page.enter_max_price(max_price)
        self.category_page.click_show_products()
        self.assertTrue(self.category_page.check_products_filtered_by_min_and_max_price(min_price, max_price))

    @data('krem', 'szampon', 'odżywka')
    def test_find_by_product_name(self, searching_product):
        self.category_page.accept_private_policy()
        self.category_page.click_search_product_input()
        self.category_page.enter_searching_product(searching_product)
        self.assertTrue(self.category_page.check_if_product_contains_searching_text(searching_product))

    @data("BIELENDA", "ALTERRA", "CATRICE", "ISANA")
    def test_find_by_product_brand(self, brand):
        self.category_page.accept_private_policy()
        self.category_page.click_checkbox(brand)
        self.category_page.scroll_and_click_show_products()
        self.category_page.scroll_to_brand_label()
        self.assertTrue(self.category_page.check_if_product_contains_searching_brand(brand))

    def test_sort_by_desc_price(self):
        self.category_page.accept_private_policy()
        self.category_page.click_sorting_by_desc_price()
        self.assertTrue(self.category_page.check_if_products_sorted_by_desc_price())

    def test_sort_by_asc_price(self):
        self.category_page.accept_private_policy()
        self.category_page.click_sorting_by_asc_price()
        self.assertTrue(self.category_page.check_if_products_sorted_by_asc_price())

    def test_sort_by_a_z_name(self):
        self.category_page.accept_private_policy()
        self.category_page.click_sorting_by_a_z_name()
        self.assertTrue(self.category_page.check_sorting_products_by_name_a_z())

    def test_sort_by_z_a_name(self):
        self.category_page.accept_private_policy()
        self.category_page.click_sorting_by_z_a_name()
        self.assertTrue(self.category_page.check_sorting_products_by_name_z_a())
