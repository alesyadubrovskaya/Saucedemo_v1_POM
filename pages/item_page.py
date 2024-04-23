from pages.base_page import BasePage
from locators.item_locate import ItemLocate


class ItemPage(BasePage):
    def item_names_find(self):
        return self.find_elems(ItemLocate.item_name)

    def item_name_find(self):
        return self.find_el(ItemLocate.item_name)

    def item_descrs_find(self):
        return self.find_elems(ItemLocate.item_descr)

    def item_descr_find(self):
        return self.find_el(ItemLocate.item_descr)

    def item_prices_find(self):
        return self.find_elems(ItemLocate.item_price)

    def item_price_find(self):
        return self.find_el(ItemLocate.item_price)

    def item_imgs_find(self):
        return self.find_elems(ItemLocate.item_img)

    def item_img_find(self):
        return self.find_el(ItemLocate.item_img)

    def item_adds_find(self):
        return self.find_elems(ItemLocate.add_button_item)

    def item_add_find(self):
        return self.find_el(ItemLocate.add_button_item)

    def item_removes_find(self):
        return self.find_elems(ItemLocate.remove_button_item)

    def item_remove_find(self):
        return self.find_el(ItemLocate.remove_button_item)

    def item_backs_find(self):
        return self.find_elems(ItemLocate.go_back)

    def item_back_find(self):
        return self.find_el(ItemLocate.go_back)