from selenium.webdriver.common.by import By
from Homework_06.page_objects.BasePage import BasePage


class ProductPage(BasePage):

    # Locators
    CURRENCY_ACTIVE = (By.CSS_SELECTOR, "#form-currency .btn-group strong")
    CURRENCY_MENU = (By.CSS_SELECTOR, "#form-currency .btn-group button")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, "#form-currency .btn-group .dropdown-menu button")
    IMAGE = (By.CSS_SELECTOR, ".col-sm-8 img")
    DESCRIPTION = (By.LINK_TEXT, "Description")
    REVIEWS = (By.PARTIAL_LINK_TEXT, "Reviews")
    CONTENT = (By.ID, "content")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#content .col-sm-4 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content .col-sm-4 ul:nth-child(4) li:nth-child(2) h2")
    ADD_TO_CART_BTN = (By.ID, "button-cart")

    # Supported currencies
    CURRENCIES = ("€", "£", "$")

    # Expected values
    EXPECTED_PRICE = {"€": "84.35€", "£": "£73.92", "$": "$98.00"}

    @property
    def _get_currency(self):
        return self._check_element_visible(self.CURRENCY_ACTIVE).text

    def _switch_currency(self, currency):
        index = self.CURRENCIES.index(currency)
        self._check_element_clickable(self.CURRENCY_MENU).click()
        self._find_elements(self.CURRENCY_OPTIONS)[index].click()
