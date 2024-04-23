from pages.base_page import BasePage
from locators.order_locate import OrderLocate, OrderData


class OrderPage(BasePage):
    def order_fname(self):
        return self.is_visible(OrderLocate.fname_field)

    def order_lname(self):
        return self.is_visible(OrderLocate.lname_field)

    def order_zip(self):
        return self.is_visible(OrderLocate.zip_field)

    def order_checkout(self):
        return self.is_clickable(OrderLocate.checkout_button)

    def order_continue(self):
        return self.is_clickable(OrderLocate.confirm_button)

    def order_finish(self):
        return self.is_clickable(OrderLocate.finish_button)

    def order_cancel(self):
        return self.is_clickable(OrderLocate.cancel_button)

    @staticmethod
    def complete_thanks():
        return OrderData.thanks_head
