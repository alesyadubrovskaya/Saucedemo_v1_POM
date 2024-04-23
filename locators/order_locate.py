class OrderLocate:
    checkout_button = ('xpath', '//*[@class="btn_action checkout_button"]')
    fname_field = ('xpath', '//*[@id="first-name"]')
    lname_field = ('xpath', '//*[@id="last-name"]')
    zip_field = ('xpath', '//*[@id="postal-code"]')
    confirm_button = ('xpath', '//*[@type="submit"]')
    finish_button = ('xpath', '//*[@class="btn_action cart_button"]')
    cancel_button = ('xpath', '//button[@class="cart_cancel_link btn_secondary"]')
    thanks_header = ('xpath', '//h2')
    thanks_icon = ('xpath', '//img[@class = "pony_express"]')


class OrderData:
    fname = 'Alex'
    lname = 'Dubr'
    zip = '123456789'
    error_order_1 = 'Error: First Name is required'
    error_order_2 = 'Error: Last Name is required'
    error_order_3 = 'Error: Postal Code is required'
    thanks_head = 'THANK YOU FOR YOUR ORDER'
    thanks_img = './img/pony-express.png'
