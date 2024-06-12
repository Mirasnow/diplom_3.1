import allure
from pages.forgot_password_page import ForgotPasswordPage
from data import Urls


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Проверка, что нажатие на кнопку "Восстановить пароль" открывает страницу восстановления пароля')
    def test_click_on_pass_recovery_button_opens_recovery_page (self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.recover_password()
        forgot_page.wait_for_recovery_page_to_load(driver)
        result = forgot_page.get_current_url()
        assert result == Urls.reset_password_url


    @allure.title('Проверка перехода на страницу "Сброс пароля"')
    @allure.description('Проверка, что после ввода электронной почты и нажатия на кнопку "Восстановить пароль" '
                        'открывается страница "Сброс пароля"')
    def test_input_email_and_click_on_pass_recovery_button_opens_pass_page(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.page_recover()
        result = forgot_page.get_current_url()
        assert result == Urls.forgot_password_url


    @allure.title('Проверка фокуса на поле ввода пароля')
    @allure.description('Проверка, что после нажатия на кнопку "Показать/скрыть пароль"'
                        'подсвечивается поле ввода пароля на странице "Сброс пароля"')
    def test_highlight_pass_entry_field(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.hide_password()
        assert forgot_page.is_password_field_highlighted()