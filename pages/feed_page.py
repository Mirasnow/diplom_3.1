from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from helpers import CreateOrder
from helpers import CreateNewUser
import allure
from data import Urls
from locators.main_page_locators import MainPageLocators as Mpl
from locators.feed_page_locators import FeedPageLocators as Fpl


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Открытие окна с деталями заказа')
    def click_order_new_window(self):
        self.click_on_element(Mpl.feed_button)
        self.click_on_element(Fpl.orders_number)


    def find_element(self, driver):
        element = driver.find_element(*Fpl.current_order_number)
        return element.text != ""


    @allure.step('Получение номера заказа в ленте заказов')
    def user_orders_in_feed(self, create_user):
        self.click_on_element(Mpl.feed_button)
        responce = CreateOrder.create_order_with_auth_with_ingr(create_user)
        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        self.click_on_element(Fpl.orders_number)
        order_ui = self.get_text_from_element(Fpl.current_order_number)
        order_ui = order_ui[2:]
        return order_number, order_ui


    @allure.step('Увеличение счетчика')
    def count_increase(self, create_user, locator_count_total):
        self.click_on_element(Mpl.feed_button)
        count_before_order = self.get_text_from_element(locator_count_total)
        CreateOrder.create_order_with_auth_with_ingr(create_user)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Urls.feed_url))
        count_after_order = self.get_text_from_element(locator_count_total)
        return count_before_order, count_after_order


    @allure.step('Получение новера заказа в работе')
    def number_order_in_progress(self, create_user):
        self.click_on_element(Mpl.feed_button)
        responce = CreateOrder.create_order_with_auth_with_ingr(create_user)
        order_ui = self.get_text_from_element(Fpl.in_progress_order)
        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        return order_number, order_ui