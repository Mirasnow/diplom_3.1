import allure
from data import Urls
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка перехода на страницу "Профиль"')
    @allure.description('Проверка, что нажатие на кнопку "Личный кабинет" в заголовке открывает страницу "Профиль"')
    def test_click_on_account_button_opens_profile_page(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.transfer_to_cabinet()
        result = profile_page.get_current_url()
        assert result == Urls.login_url


    @allure.title('Проверка перехода на страницу "История заказов"')
    @allure.description('Проверка, что нажатие на ссылку "История заказов" в профиле открывает страницу "История заказов"')
    def test_click_on_order_history_url_opens_orders_history_page(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.history_orders()
        result = profile_page.get_current_url()
        assert result == Urls.order_history_url


    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка, что нажатие на кнопку "Выход" в профиле приводит к выходу из аккаунта')
    def test_click_on_exit_url_logs_out_from_account(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.authorization_and_exit()
        profile_page.wait_for_login_page_to_load(driver)
        result = profile_page.get_current_url()
        assert result == Urls.login_url