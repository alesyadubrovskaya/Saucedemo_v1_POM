from pages.base_page import BasePage
from locators.cart_locate import CartLocate
from locators.inventory_locate import InventLocate



class CartPage(BasePage):
    def cart_head(self):
        return self.is_visible(CartLocate.cart_head)

    def cart_badge_visible(self):
        return self.is_visible(CartLocate.cart_count)

    def cart_badge_invisible(self):
        return self.is_invisible(CartLocate.cart_count)

    def cart_cont(self):
        return self.is_visible(CartLocate.cart_container)

    def cart_quantity(self):
        return self.is_visible(CartLocate.cart_quant)

    def cart_quantities_find(self):
        return self.find_elems(CartLocate.cart_quant)

    def cart_quantity_find(self):
        return self.find_el(CartLocate.cart_quant)

    def cart_icons_find(self):
        return self.find_elems(CartLocate.cart_button)

    def cart_icon_find(self):
        return self.find_el(CartLocate.cart_button)

    def cart_removes_find(self):
        return self.find_elems(CartLocate.remove_button_cart)

    def cart_remove_find(self):
        return self.find_el(CartLocate.remove_button_cart)

    def cart_return(self):
        return self.is_clickable(CartLocate.shop_button)

    def cart_item_names_find(self):
        return self.find_elems(InventLocate.inv_name)

    def cart_item_name_find(self):
        return self.find_el(InventLocate.inv_name)

    def cart_item_descrs_find(self):
        return self.find_elems(InventLocate.inv_descr)

    def cart_item_descr_find(self):
        return self.find_el(InventLocate.inv_descr)

    def cart_item_prices_find(self):
        return self.find_elems(InventLocate.inv_price)

    def cart_item_price_find(self):
        return self.find_el(InventLocate.inv_price)

    def cart_items_cards(self):
        return self.find_elems(CartLocate.cart_card)
