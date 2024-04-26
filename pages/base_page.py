import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 10)

    def open(self):
        with allure.step('open the page'):
            self.browser.get(self.url)

    def refresh(self):
        with allure.step('refresh the page'):
            return self.browser.refresh()

    # go back the browser on the URL set-up
    def go_back(self):
        with allure.step('go back to the previous page'):
            return self.browser.back()

    # find the elements set-up
    def find_elems(self, locator) -> list[WebElement]:
        return self.browser.find_elements(*locator)

    # find one element set-up
    def find_el(self, locator) -> WebElement:
        return self.browser.find_element(*locator)

    # see if the element is visible set-up
    def is_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    # see if the element is invisible set-up
    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def visibility(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of(locator))

    # see if the element is clickable set-up
    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))




