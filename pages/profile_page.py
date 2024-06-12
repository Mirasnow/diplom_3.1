from data import CommonData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators as Mpl
from locators.profile_page_locators import ProfilePageLocators as Ppl
from locators.login_page_locators import LoginPageLocators as Lpl
from pages.base_page import BasePage
import allure
from data import Urls


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Переход в личный кабинет')
    def transfer_to_cabinet(self):
        self.click_on_element(Mpl.account_button)


    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Открытие истории заказов')
    def history_orders(self):
        self.click_on_element(Mpl.account_button)
        self.set_text_to_element(Lpl.email_input_field, CommonData.test_email)
        self.set_text_to_element(Lpl.password_input_field, CommonData.test_user_password)
        self.click_on_element(Lpl.sign_in_button)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Urls.main_url))
        self.click_on_element(Mpl.account_button)
        self.click_on_element(Ppl.orders_history_url)


    @allure.step('Разлогин пользователя')
    def authorization_and_exit(self):
        self.click_on_element(Mpl.account_button)
        self.set_text_to_element(Lpl.email_input_field, CommonData.test_email)
        self.set_text_to_element(Lpl.password_input_field, CommonData.test_user_password)
        self.click_on_element(Lpl.sign_in_button)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Urls.main_url))
        self.click_on_element(Mpl.account_button)
        self.click_on_element(Ppl.exit_button)


    def wait_for_login_page_to_load(self, driver):
        wait = WebDriverWait(driver,3)
        wait.until(EC.url_to_be(Urls.login_url))