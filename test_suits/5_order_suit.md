# ЗАКАЗ ТОВАРОВ

### Позитивные тесты:

**№5_1. Заказ одного товара с валидными данными заказчика**
(auth_tests.py::test_order_item_ok)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Нажать "ADD TO CART" возле любого товара;
_*Ожидаемый промежуточный результат:_
Товар добавлен в корзину, иконка количества товара в корзине появляется со значением 1.
2. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html с информацией о
добавленном товаре.
3. Нажать "CHECKOUT";
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-one.html с формой
указания сведений о заказчике.
4. Ввести в поле First Name 'Alex';
5. Ввести в поле Last Name 'Dubr';
6. Ввести в поле Zip/Postal Code '123456';
7. Кликнуть "CONTINUE";
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-two.html с данными
о заказе.
8. Кликнуть "FINISH";

_Ожидаемый результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-complete.html с 
благодарностью и изображением.



### Негативные тесты:

**№5_2. Заказ нескольких товаров с невалидными данными заказчика (ОБНАРУЖЕН ДЕФЕКТ)**
(auth_tests.py::test_order_items_wrong)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Нажать "ADD TO CART" возле любых товаров;
_*Ожидаемый промежуточный результат:_
Товары добавлены в корзину, иконка количества товаров в корзине появляется со значением добваленных в 
корзину товаров.
2. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html с информацией о
добавленных товарах.
3. Нажать "CHECKOUT".

_Ожидаемый результат:_
Подтверждение формы сведений о заказчике провалено, появляются ошибки о неверно заполненных полях;
перенаправления не происходит.

_Реальный результат:_
После нажатия кнопки "CONTINUE" происходит перенаправление на страницу 
https://www.saucedemo.com/v1/checkout-step-two.html с данными о заказе.
После нажатия кнопки "FINISH" происходит перенаправление на страницу 
https://www.saucedemo.com/v1/checkout-complete.html с благодарностью и изображением.



**№5_3. Заказ пустой корзины с пустой формой сведений о заказчике**
(auth_tests.py::test_order_empty)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html.
3. Нажать "CHECKOUT".

_Ожидаемый результат:_
Перенаправление провалено; появляется ошибка о необходимости пополнить корзину.

_Реальный результат:_
После нажатия кнопки "CHECKOUT" происходит перенаправление на страницу 
https://www.saucedemo.com/v1/checkout-step-one.html с формой указания сведений о заказчике.
После нажатия кнопки "CONTINUE" при пустой форме подтверждение данных провалено; появляется ошибка 
"Error: First Name is required"; перенаправления не происходит.



**№5_4. Заказ одного товара с пустым именем заказчика**
(auth_tests.py::test_order_empty_fname)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html.
3. Нажать "CHECKOUT";
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-one.html с формой
указания сведений о заказчике.
4. Оставить поле First Name пустым;
5. Ввести в поле Last Name 'Dubr';
6. Ввести в поле Zip/Postal Code '123456';
7. Кликнуть "CONTINUE".

_Ожидаемый результат:_
Подтверждение данных провалено; появляется ошибка "Error: First Name is required"; 
перенаправления не происходит.



**№5_5. Заказ одного товара с пустой фамилией заказчика**
(auth_tests.py::test_order_empty_lname)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html.
3. Нажать "CHECKOUT";
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-one.html с формой
указания сведений о заказчике.
4. Ввести в поле First Name 'Alex';
5. Оставить поле Last Name пустым;
6. Ввести в поле Zip/Postal Code '123456';
7. Кликнуть "CONTINUE".

_Ожидаемый результат:_
Подтверждение данных провалено; появляется ошибка "Error: Last Name is required"; 
перенаправления не происходит.



**№5_6. Заказ одного товара с пустым почтовым индексом заказчика**
(auth_tests.py::test_order_empty_lname)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html.
3. Нажать "CHECKOUT";
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-one.html с формой
указания сведений о заказчике.
4. Ввести в поле First Name 'Alex';
5. Ввести в поле Last Name 'Dubr'';
6. Оставить поле Zip/Postal Code пустым;
7. Кликнуть "CONTINUE".

_Ожидаемый результат:_
Подтверждение данных провалено; появляется ошибка "Error: Postal Code is required"; 
перенаправления не происходит.



**№5_7. Заказ пустой корзины с валидными данными заказчика (ОБНАРУЖЕН ДЕФЕКТ)**
(auth_tests.py::test_order_empty_ok)

Предусловие: Успешно авторизоваться в системе сайта с перенаправлением на страницу 
https://www.saucedemo.com/v1/inventory.html 

Шаги:
1. Кликнуть на иконку корзины;
_*Ожидаемый промежуточный результат:_
Происходит перенаправление на страницу https://www.saucedemo.com/v1/cart.html.
3. Нажать "CHECKOUT".

_Ожидаемый результат:_
Перенаправление провалено; появляется ошибка о необходимости пополнить корзину.

_Реальный результат:_
После нажатия кнопки "CHECKOUT" происходит перенаправление на страницу 
https://www.saucedemo.com/v1/checkout-step-one.html с формой указания сведений о заказчике.
После нажатия кнопки "CONTINUE" при заполненной форме сведений о заказчике
происходит перенаправление на страницу https://www.saucedemo.com/v1/checkout-step-two.html с данными 
о заказе.
После нажатия кнопки "FINISH" происходит перенаправление на страницу 
https://www.saucedemo.com/v1/checkout-complete.html с благодарностью и изображением.

