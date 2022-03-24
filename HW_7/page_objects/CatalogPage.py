from selenium.webdriver.common.by import By
from Homework_07.page_objects.BasePage import BasePage


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
