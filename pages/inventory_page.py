from pages.base_page import BasePage
from locators.inventory_locate import InventLocate

class InventoryPage(BasePage):
    def invent_header(self):
        return self.is_visible(InventLocate.inv_head)

    def invent_cards_find(self):
        return self.find_elems(InventLocate.inv_goods)

    def invent_card_find(self):
        return self.find_el(InventLocate.inv_goods)

    def invent_names_find(self):
        return self.find_elems(InventLocate.inv_name)

    def invent_name_find(self):
        return self.find_el(InventLocate.inv_name)

    def invent_descrs_find(self):
        return self.find_elems(InventLocate.inv_descr)

    def invent_descr_find(self):
        return self.find_el(InventLocate.inv_descr)

    def invent_prices_find(self):
        return self.find_elems(InventLocate.inv_price)

    def invent_price_find(self):
        return self.find_el(InventLocate.inv_price)

    def invent_imgs_find(self):
        return self.find_elems(InventLocate.inv_img)

    def invent_img_find(self):
        return self.find_el(InventLocate.inv_img)

    def invent_adds_find(self):
        return self.find_elems(InventLocate.add_button)

    def invent_add_find(self):
        return self.find_el(InventLocate.add_button)

    def invent_removes_find(self):
        return self.find_elems(InventLocate.remove_button)

    def invent_remove_find(self):
        return self.find_el(InventLocate.remove_button)