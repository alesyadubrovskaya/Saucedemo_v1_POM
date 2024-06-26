# РАБОТА БОКОВОГО МЕНЮ 

### Позитивные тесты:

**№3_1. Проверка опции Logout**
(auth_tests.py::test_logout)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html (или находиться на других страницах сайта).

Шаги:
1. Кликнуть на иконку бокового меню;
2. Выбрать опцию Logout.

_Ожидаемый результат:_
Происходит перенаправление на страницу авторизации https://www.saucedemo.com/v1/index.html.



**№3_2. Проверка опции About**
(auth_tests.py::test_about)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html (или находиться на других страницах сайта).

Шаги:
1. Кликнуть на иконку бокового меню;
2. Выбрать опцию About.

_Ожидаемый результат:_
Происходит перенаправление на страницу авторизации https://saucelabs.com/.



**№3_3. Проверка опции Reset App State**
(auth_tests.py::test_reset)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html.

Шаги:
1. Добавить товар(ы) в корзину;
2. Кликнуть на иконку бокового меню;
3. Выбрать опцию Reset App State;
4. Обновить страницу (в случае нахождения на любой другой странице).

_Ожидаемый результат:_
Иконка количества товаров в корзине исчезает, корзина пуста.



**№3_4. Проверка опции All Items**
(auth_tests.py::test_allitems)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html.

Шаги:
1. Зайти на любую другую страницу сайта (например, на страницу товара Sauce Labs Bike Light);
2. Кликнуть на иконку бокового меню;
3. Выбрать опцию All Items.

_Ожидаемый результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/inventory.html.


