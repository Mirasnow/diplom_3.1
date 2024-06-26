## Дипломный проект. Задание 3: Page Object Model

### Тестирование веб-приложения Stellar Burgers. 

### Структура проекта:

locators - содержит файлы с локатоми разных страниц сайта https://stellarburgers.nomoreparties.site/
pages - директория pages содержит в себе методы страниц сайта
tests - пакет, содержащий тесты, разделенные по классам:

1. test_feed_page.py

Раздел «Лента заказов»

Проверки:
- если кликнуть на заказ, откроется всплывающее окно с деталями,
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
- при создании нового заказа счётчик Выполнено за всё время увеличивается,
- при создании нового заказа счётчик Выполнено за сегодня увеличивается,
- после оформления заказа его номер появляется в разделе В работе.

2. test_forgot_password_page.py

Восстановление пароля

Проверки:
- переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
- ввод почты и клик по кнопке «Восстановить»,
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.

3. test_main_page.py

Основной функционал

Проверки:
- переход по клику на «Конструктор»,
- переход по клику на «Лента заказов»,
- если кликнуть на ингредиент, появится всплывающее окно с деталями,
- всплывающее окно закрывается кликом по крестику,
- при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
- залогиненный пользователь может оформить заказ.

4. test_profile_page.py

Личный кабинет 

Проверки:
- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта.

6. conftest.py

Содержит фикстуру create_user


Также в корневой папке проекта находятся:
файл data.py c тестовыми данными,
файл requirements.txt c зависимостями проекта и
файл .gitignore.


### Запуск автотестов:
**Установка зависимостей** 

> `$ pip install -r requirements.txt`

**Генерация Allure-отчёта**

> `$ pytest tests --alluredir=allure_results`

> `$ allure serve allure_results`