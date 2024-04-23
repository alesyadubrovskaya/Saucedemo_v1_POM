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
        self.browser.get(self.url)

    def refresh(self):
        return self.browser.refresh()

    def find_elems(self, locator) -> list[WebElement]:
        return self.browser.find_elements(*locator)

    def find_el(self, locator) -> WebElement:
        return self.browser.find_element(*locator)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def visibility(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of(locator))

    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))




