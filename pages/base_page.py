import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверка видимости указанного элемента')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажатие на указанный элемент')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Заполнение указанного поля данными')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.send_keys(text)

    @allure.step('Возврат текста указанного элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return element.text

    def get_element_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).text

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, drag_element, drop_element):
        ActionChains(self.driver).drag_and_drop(drag_element, drop_element).perform()