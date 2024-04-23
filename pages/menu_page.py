from pages.base_page import BasePage
from locators.sidebar_locate import SidebarLocate


class SidebarPage(BasePage):
    def open_menu(self):
        return self.find_el(SidebarLocate.sidebar)

    def allitem_opt(self):
        return self.is_clickable(SidebarLocate.allitems)

    def about_opt(self):
        return self.is_clickable(SidebarLocate.about)

    def logout_opt(self):
        return self.is_clickable(SidebarLocate.logout)

    def reset_opt(self):
        return self.is_clickable(SidebarLocate.reset)

    def close_menu(self):
        return self.is_clickable(SidebarLocate.close_sidebar)