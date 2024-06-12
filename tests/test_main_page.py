import allure
from pages.main_page import MainPage
from data import Urls


class TestMainPage:

    @allure.title('Проверка перехода на страницy "Лента заказов"')
    @allure.description('Тест на проверку, что нажатие на кнопку "Лента заказов" в заголовке '
                        'перенаправляет на соответствующую страницу')
    def test_transfer_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.transfer_to_feed()
        main_page.wait_for_feed_page_to_load(driver)
        result = main_page.get_current_url()
        assert result == Urls.feed_url


    @allure.title('Проверка перехода на страницы "Конструктор"')
    @allure.description('Тест на проверку, что нажатие на кнопку "Конструктор" в заголовке '
                        'перенаправляет на соответствующую страницу')
    def test_transfer_to_cons(self, driver):
        main_page = MainPage(driver)
        main_page.transfer_to_constructor()
        main_page.wait_for_main_page_to_load(driver)
        result = main_page.get_current_url()
        assert result == Urls.main_url


    @allure.title('Проверка открытия поп-апа с информацией об ингредиенте')
    @allure.description('Проверка, что нажатие на ингредиент открывает поп-ап с информацией об ингредиенте')
    def test_new_window(self, driver):
        main_page = MainPage(driver)
        result = main_page.new_window()
        assert result == "Детали ингредиента"


    @allure.title('Проверка закрытия поп-апа с информацией об ингредиенте')
    @allure.description('Проверка, что нажатие на кнопку закрытия поп-апа с информацией об ингредиенте закрывает окно')
    def test_close_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.close_new_window()
        element_class = main_page.find_element_class(driver)
        assert element_class == 'Modal_modal__P3_V5'


    @allure.title('Проверка увеличения счетчика ингредиента')
    @allure.description('Проверка, что добавление ингредиента в заказ увеличивает его счетчик на определенное значение')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient()
        element = main_page.get_counter()
        assert element == "2"


    @allure.title('Проверка, что авторизованный пользователь может сделать заказ')
    @allure.description('Проверка, что авторизованный пользователь может оформить заказ')
    def test_create_order(self, driver):
        main_page = MainPage(driver)
        main_page.create_order()
        order_number = main_page.find_order_number(driver)
        assert order_number != ''