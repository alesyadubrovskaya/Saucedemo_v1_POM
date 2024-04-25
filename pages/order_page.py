import pytest
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

    def order_item_quant(self):
        return self.find_el(OrderLocate.order_quant)

    def order_item_quants(self):
        return self.find_elems(OrderLocate.order_quant)

    def subtotal(self):
        return self.is_visible(OrderLocate.sub_total)

    def tax(self):
        return self.is_visible(OrderLocate.tax)

    def total(self):
        return self.is_visible(OrderLocate.total)

    def order_finish(self):
        return self.is_clickable(OrderLocate.finish_button)

    def order_cancel(self):
        return self.is_clickable(OrderLocate.cancel_button)

    def order_thanks_img(self):
        return self.is_visible(OrderLocate.thanks_icon)

    @staticmethod
    def complete_thanks():
        return OrderData.thanks_head

    @staticmethod
    def empty_order_form_error():
        return OrderData.error_order_1

    @staticmethod
    def empty_order_lname_form_error():
        return OrderData.error_order_2

    @staticmethod
    def empty_order_zip_form_error():
        return OrderData.error_order_3