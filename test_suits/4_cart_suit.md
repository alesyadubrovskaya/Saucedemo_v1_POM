# ДОБАВЛЕНИЕ ТОВАРОВ В КОРЗИНУ И УДАЛЕНИЕ ИХ ИЗ НЕЕ 

### Позитивные тесты:

**№4_1. Добавление и удаление товаров через страницу товара**
(auth_tests.py::test_add_item_ip_1)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на название товара;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу товара с информацией.
2. Нажать "ADD TO CART";
_*Ожидаемый промежуточный результат:_
Товар добавлен в корзину, иконка количества товара в корзине появляется со значением 1.
3. Нажать "REMOVE".

_Ожидаемый результат:_
Иконка количества товаров в корзине исчезает, корзина пуста.



**№4_2. Добавление товаров через страницу товара и удаление их через страницу корзины**
(auth_tests.py::test_add_item_ip_2)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на название товара;
2. Нажать "ADD TO CART";
Товар добавлен в корзину, иконка количества товара в корзине появляется со значением 1.
3. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html с информацией о
добавленном товаре.
4. Нажать "REMOVE".

_Ожидаемый результат:_
Иконка количества товаров в корзине исчезает, корзина пуста.



**№4_3. Добавление и удаление товаров через страницу каталога**
(auth_tests.py::test_add_item_mp)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Нажать "ADD TO CART" любого товара;
_*Ожидаемый промежуточный результат:_
Товар добавлен в корзину, иконка количества товара в корзине появляется со значением 1.
2. Нажать "REMOVE" возле добавленного товара.

_Ожидаемый результат:_
Иконка количества товаров в корзине исчезает, корзина пуста.