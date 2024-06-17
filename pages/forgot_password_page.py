import allure
from pages.base_page import BasePage
from data import CommonData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators as Lpl
from locators.main_page_locators import MainPageLocators as Mpl
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as Fpl
from data import Urls


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Восстановелние пароля')
    def recover_password(self):
        self.click_on_element(Mpl.account_button)
        self.click_on_element(Lpl.forgot_password_button)
        self.set_text_to_element(Fpl.email_entry_field, CommonData.test_email)
        self.click_on_element(Fpl.recover_button)


    def wait_for_recovery_page_to_load(self, driver):
        wait = WebDriverWait(driver,3)
        wait.until(EC.url_to_be(Urls.reset_password_url))


    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Открытие страницы воссатновления пароля')
    def page_recover(self):
        self.click_on_element(Mpl.account_button)
        self.click_on_element(Lpl.forgot_password_button)


    @allure.step('Показ и скрытие элемента')
    def hide_password(self):
        self.click_on_element(Mpl.account_button)
        self.click_on_element(Fpl.email_entry_field)

    def is_password_field_highlighted (self):
        element = self.driver.find_element(*Fpl.email_entry_field)
        tab = element.find_element(*Lpl.email_active_field)
        tab_class = tab.get_attribute("class")
        return tab_class == 'input pr-6 pl-6 input_type_text input_size_default input_status_active'