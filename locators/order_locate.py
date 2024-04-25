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
    sub_total = ('xpath', '//div[@class = "summary_subtotal_label"]')
    tax = ('xpath', '//div[@class = "summary_tax_label"]')
    total = ('xpath', '//div[@class = "summary_total_label"]')
    order_quant = ('xpath', '//div[@class = "summary_quantity"]')


class OrderData:
    fname_ok = 'Alex'
    lname_ok = 'Dubr'
    zip_ok = '123456'
    fname_wrong = '1'
    lname_wrong = 'm'
    zip_wrong = '*'
    error_order_1 = 'Error: First Name is required'
    error_order_2 = 'Error: Last Name is required'
    error_order_3 = 'Error: Postal Code is required'
    thanks_head = 'THANK YOU FOR YOUR ORDER'
    thanks_img = 'https://www.saucedemo.com/v1/img/pony-express.png'
    tax_rate = 0.0800266755585195
