class AuthLocate:
    username_field = ('xpath', '//*[@id="user-name"]')
    password_field = ('xpath', '//*[@id="password"]')
    login_button = ('xpath', '//*[@id="login-button"]')
    error_message = ('xpath', '//*[@data-test="error"]')


class AuthData:
    username_ok = 'standard_user'
    username_glitch = 'performance_glitch_user'
    username_logout = 'locked_out_user'
    username_problem = 'problem_user'
    password_ok = 'secret_sauce'
    username_wrong = 'Alex'
    password_wrong = '123Abc+'
    login_button_text = 'LOGIN'
    error_text_1 = 'Epic sadface: Username and password do not match any user in this service'
    error_text_2 = 'Epic sadface: Username is required'
    error_text_3 = 'Epic sadface: Password is required'
    error_text_4 = 'Epic sadface: Sorry, this user has been locked out.'