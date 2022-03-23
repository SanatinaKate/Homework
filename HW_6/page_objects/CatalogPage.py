from selenium.webdriver.common.by import By
from Homework_06.page_objects.BasePage import BasePage


class CatalogPage(BasePage):

    # Locators
    CAMERAS_TITLE = (By.CSS_SELECTOR, ".col-sm-9 h2")
    LIST_VIEW = (By.ID, "list-view")
    GRID_VIEW = (By.ID, "grid-view")
    SORT_MENU = (By.CSS_SELECTOR, "#input-sort option")
    SHOW_MENU = (By.CSS_SELECTOR, "#input-limit option")
    CONTENT = (By.ID, "content")
    PRODUCTS = (By.CSS_SELECTOR, "#content div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    # Expected values
    EXPECTED_LIMITS = ["15", "25", "50", "75", "100"]
    EXPECTED_NAMES = ["Canon EOS 5D", "Nikon D300"]

    def _get_menu_options(self, locator: tuple):
        options = []
        elements = self._find_elements(locator)
        for element in elements:
            options.append(element.text)
        return options

    def _get_menu_option(self, locator: tuple, index: int):
        return self._find_elements(locator)[index].text
