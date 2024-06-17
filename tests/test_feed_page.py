import allure
import pytest
from pages.feed_page import FeedPage
from data import CommonData


class TestFeedPage:

    @allure.title('Проверка открытия поп-апа с деталями заказа')
    @allure.description('Проверка, что при нажатии на заказ открывается поп-ап с деталями заказа')
    def test_click_on_order_opens_details_popup_window(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_order_new_window()
        assert feed_page.find_element(driver)


    @allure.title('Проверка отображения заказов пользователя из "Истории заказов" на странице "Лента заказов"')
    @allure.description('Проверка, что заказы пользователя из "Истории заказов" отображаются на странице "Лента заказов"')
    def test_user_order_displayed_on_feed_page(self, driver, create_user):
        feed_page = FeedPage(driver)
        order_responce, order_ui = feed_page.user_orders_in_feed(create_user)
        assert order_responce == order_ui


    @allure.title('Проверка увеличения счетчиков заказов, выполненных за сегодня и за всё время')
    @allure.description('Проверка, что создание нового заказа увеличивает счетчики "Выполнено за сегодня" и "Выполнено за всё время"')
    @pytest.mark.parametrize('counter_locator, description', CommonData.counters)
    def test_increase_counter(self, driver, create_user, counter_locator, description):
        feed_page = FeedPage(driver)
        count_before_order, count_after_order = feed_page.count_increase(create_user, counter_locator)
        assert int(count_after_order) == int(count_before_order) + 1


    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    @allure.description('Проверка, что после размещения заказа его номер отображается в разделе "В работе"')
    def test_order_number_displayed_in_progress_section(self, driver, create_user):
        feed_page = FeedPage(driver)
        order_number, order_ui = feed_page.number_order_in_progress(create_user)
        order_ui = order_ui[1:]
        assert order_number == order_ui