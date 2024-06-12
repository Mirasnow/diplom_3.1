import allure
from pages.base_page import BasePage
from data import CommonData
from locators.main_page_locators import MainPageLocators as Mpl
from locators.login_page_locators import LoginPageLocators as Lpl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Переход на страницу заказов')
    def transfer_to_feed(self):
        self.click_on_element(Mpl.feed_button)


    def get_current_url(self):
        return self.driver.current_url


    def wait_for_feed_page_to_load(self, driver):
        wait = WebDriverWait(driver,3)
        wait.until(EC.url_to_be(Urls.feed_url))


    def wait_for_main_page_to_load(self, driver):
        wait = WebDriverWait(driver,3)
        wait.until(EC.url_to_be(Urls.main_url))


    @allure.step('Перход на страницу')
    def transfer_to_constructor(self):
        self.click_on_element(Mpl.feed_button)
        self.click_on_element(Mpl.constructor_button)


    @allure.step('Открытие нового окна')
    def new_window(self):
        self.click_on_element(Mpl.object_order)
        return self.get_text_from_element(Mpl.ingredient_details)


    @allure.step('Закрытие нового окна')
    def close_new_window(self):
        self.click_on_element(Mpl.object_order)
        self.click_on_element(Mpl.window_button_class)


    def find_element_class(self, driver):
        element = driver.find_element(*Mpl.section_class)
        return element.get_attribute("class")


    @allure.step('Добавление ингридиента')
    def add_ingredient(self):
        ingredient = self.find_element_with_wait(Mpl.object_order)
        add_to_order = self.find_element_with_wait(Mpl.base_order_button)
        self.drag_and_drop(ingredient, add_to_order)


    @allure.step("Получение счетчика ингредиента")
    def get_counter(self):
        return self.get_element_text(Mpl.ingredient_counter)


    @allure.step('Создание заказа')
    def create_order(self):
        self.click_on_element(Mpl.account_button)
        self.set_text_to_element(Lpl.email_input_field, CommonData.test_email)
        self.set_text_to_element(Lpl.password_input_field, CommonData.test_user_password)
        self.click_on_element(Lpl.sign_in_button)
        self.add_ingredient()
        self.click_on_element(Mpl.place_order_button)


    def find_order_number(self, driver):
        element = driver.find_element(*Mpl.order_number)
        return element.text != ''