from selenium.webdriver.common.by import By
from Homework_06.page_objects.BasePage import BasePage


class MainPage(BasePage):

    # Locators
    LOGO = (By.CSS_SELECTOR, "#logo a")
    CART_BTN = (By.CSS_SELECTOR, ".col-sm-3 button[type='button']")
    CART_MENU = (By.CSS_SELECTOR, ".dropdown-menu.pull-right")
    SEARCH_BTN = (By.CLASS_NAME, "input-group-btn")
    CONTENT = (By.ID, "content")
    FEATURED = (By.CSS_SELECTOR, "#content div.row .product-layout")
    FEATURED_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    # Expected values
    EXPECTED_NAMES = ["MacBook", "iPhone", "Apple Cinema 30\"", "Canon EOS 5D"]
