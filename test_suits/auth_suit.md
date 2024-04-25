# АВТОРИЗАЦИЯ

### Позитивные тесты:

**№1_1. Авторизация под данными 'standard_user'**
(auth_tests.py::test_login_standard)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'standard_user';
2. Ввести в поле Password 'secret_sauce';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация пройдена успешно, происходит перенаправление на страницу каталога
https://www.saucedemo.com/v1/inventory.html.



**№1_2. Авторизация под данными 'locked_out_user'**
(auth_tests.py::test_login_lockedout)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'locked_out_user';
2. Ввести в поле Password 'secret_sauce';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация провалена; появляется ошибка "Epic sadface: Sorry, this user has been locked out.";
перенаправления не происходит.



**№1_3. Авторизация под данными 'problem_user'**
(auth_tests.py::test_login_problem)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'problem_user';
2. Ввести в поле Password 'secret_sauce';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация пройдена успешно, происходит перенаправление на страницу каталога
https://www.saucedemo.com/v1/inventory.html; изображения товаров не отображаются.



**№1_4. Авторизация под данными 'performance_glitch_user'**
(auth_tests.py::test_login_glitch)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'performance_glitch_user';
2. Ввести в поле Password 'secret_sauce';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация пройдена успешно, перенаправление на страницу каталога
https://www.saucedemo.com/v1/inventory.html происходит с задержкой.



### Негативные тесты:

**№1_5. Авторизация с некорректными данными**
(auth_tests.py::test_login_wrong)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'Alex';
2. Ввести в поле Password '123Abc+';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация провалена; появляется ошибка "Epic sadface: Username and password 
do not match any user in this service"; перенаправления не происходит.



**№1_6. Авторизация с пустой формой авторизации**
(auth_tests.py::test_login_empty)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Оставить поле Username пустым;
2. Оставить Password пустым;
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация провалена; появляется ошибка "Epic sadface: Username is required"; 
перенаправления не происходит.



**№1_7. Авторизация с пустым полем Username**
(auth_tests.py::test_login_empty_name)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Оставить поле Username пустым;
2. Ввести в поле Password 'secret_sauce';
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация провалена; появляется ошибка "Epic sadface: Username is required"; 
перенаправления не происходит.



**№1_8. Авторизация с пустым полем Password**
(auth_tests.py::test_login_empty_pass)

Предусловие: Открыть страницу авторизации 
https://www.saucedemo.com/v1/index.html.

Шаги:
1. Ввести в поле Username 'standard_user';
2. Оставить Password пустым;
3. Кликнуть кнопку LOGIN.

_Ожидаемый результат:_
Авторизация провалена; появляется ошибка "Epic sadface: Password is required"; 
перенаправления не происходит.

