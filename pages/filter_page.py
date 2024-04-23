from pages.base_page import BasePage
from locators.filter_locate import FilterLocate


class FilterPage(BasePage):
    def za_opt(self):
        return self.is_visible(FilterLocate.za)

    def lohi_opt(self):
        return self.is_visible(FilterLocate.lohi)

    def hilo_opt(self):
        return self.is_visible(FilterLocate.hilo)

    def az_opt(self):
        return self.is_visible(FilterLocate.az)