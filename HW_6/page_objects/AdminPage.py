from selenium.webdriver.common.by import By
from Homework_06.page_objects.BasePage import BasePage


class AdminPage(BasePage):

    # Locators
    LOGO = (By.CSS_SELECTOR, ".navbar-brand img")
    LOGIN_PANEL_TITLE = (By.CSS_SELECTOR, "#content .panel-heading h1")
    USERNAME_TITLE = (By.CSS_SELECTOR, "#content .panel-body div:nth-child(1) label")
    PASSWORD_TITLE = (By.CSS_SELECTOR, "#content .panel-body div:nth-child(2) label")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    NAVIGATION_MENU = (By.ID, "navigation")
    MENU_CATALOG = (By.ID, "menu-catalog")
    PRODUCTS = (By.CSS_SELECTOR, "#menu-catalog ul li:nth-child(2) a")
    PRODUCT_ADD_BTN = (By.CSS_SELECTOR, ".pull-right a")
    PRODUCT_DELETE_BTN = (By.CSS_SELECTOR, ".pull-right button:nth-child(4)")
    PRODUCT_SAVE_BTN = (By.CSS_SELECTOR, ".pull-right button")
    FILTER_TITLE = (By.CSS_SELECTOR, "#filter-product .panel-title")
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, "#filter-product #input-name")
    FILTER_MODEL = (By.CSS_SELECTOR, "#filter-product #input-model")
    FILTER_PRICE = (By.CSS_SELECTOR, "#filter-product #input-price")
    FILTER_QUANTITY = (By.CSS_SELECTOR, "#filter-product #input-quantity")
    FILTER_APPLY_BTN = (By.ID, "button-filter")
    PRODUCT_ADD_TITLE = (By.CSS_SELECTOR, ".container-fluid .panel-title")
    PRODUCT_GENERAL_TAB = (By.CSS_SELECTOR, "#form-product ul li:nth-child(1) a")
    PRODUCT_DATA_TAB = (By.CSS_SELECTOR, "#form-product ul li:nth-child(2) a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".tab-content #input-name1")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".tab-content .note-editable")
    PRODUCT_META_TAG_TITLE = (By.CSS_SELECTOR, ".tab-content #input-meta-title1")
    PRODUCT_TAGS = (By.CSS_SELECTOR, ".tab-content #input-tag1")
    PRODUCT_MODEL = (By.CSS_SELECTOR, ".tab-content #input-model")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".tab-content #input-price")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".tab-content #input-quantity")
    PRODUCT_WEIGHT = (By.CSS_SELECTOR, ".tab-content #input-weight")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".container-fluid .alert")
    RESULT_HEAD_CHECKBOX = (By.CSS_SELECTOR, "#form-product table thead input[type='checkbox']")
    RESULT_BODY_DATA = (By.CSS_SELECTOR, "#form-product table tbody tr td")

    # Product data
    PRODUCT = {
        "Name": "Test Name",
        "Description": "Test Description",
        "Meta Tag Title": "Test Meta Tag Title",
        "Tags": "Test Tag1, Test Tag2",
        "Model": "Test Model",
        "Price": 100.0,
        "Quantity": 10,
        "Weight": 1.0
    }

    # Alerts
    ALERT_SUCCESS = "Success: You have modified products!"
    ALERT_WARNING = "Warning: You do not have permission to modify products!"

    # Admin credentials
    ADMIN_USERNAME = "user"
    ADMIN_PASSWORD = "bitnami"

    def _login(self, username, password):
        self._fill_input(self.USERNAME_INPUT, username)
        self._fill_input(self.PASSWORD_INPUT, password)
        self._click_element(self.LOGIN_BTN)
        self._check_element_visible(self.NAVIGATION_MENU)

    def _assert_alert_message(self):
        alert_message = self._check_element_visible(self.ALERT_MESSAGE).text
        assert (self.ALERT_SUCCESS in alert_message) or (self.ALERT_WARNING in alert_message)

    def _add_product(self, product):
        self._click_element(self.MENU_CATALOG)
        self._click_element(self.PRODUCTS)
        self._click_element(self.PRODUCT_ADD_BTN)
        self._check_element_text(self.PRODUCT_ADD_TITLE, "Add Product")
        self._click_element(self.PRODUCT_GENERAL_TAB)
        self._fill_input(self.PRODUCT_NAME, product["Name"])
        self._fill_input(self.PRODUCT_DESCRIPTION, product["Description"])
        self._fill_input(self.PRODUCT_META_TAG_TITLE, product["Meta Tag Title"])
        self._fill_input(self.PRODUCT_TAGS, product["Tags"])
        self._click_element(self.PRODUCT_DATA_TAB)
        self._fill_input(self.PRODUCT_MODEL, product["Model"])
        self._fill_input(self.PRODUCT_PRICE, product["Price"])
        self._fill_input(self.PRODUCT_QUANTITY, product["Quantity"])
        self._fill_input(self.PRODUCT_WEIGHT, product["Weight"])
        self._click_element(self.PRODUCT_SAVE_BTN)
        self._assert_alert_message()

    def _delete_product(self, product):
        self._click_element(self.MENU_CATALOG)
        self._click_element(self.PRODUCTS)
        self._check_element_text(self.FILTER_TITLE, "Filter")
        self._fill_input(self.FILTER_PRODUCT_NAME, product["Name"])
        self._fill_input(self.FILTER_MODEL, product["Model"])
        self._fill_input(self.FILTER_PRICE, product["Price"])
        self._fill_input(self.FILTER_QUANTITY, product["Quantity"])
        self._click_element(self.FILTER_APPLY_BTN)
        data = self._find_elements(self.RESULT_BODY_DATA)
        if len(data) == 1:
            assert data[0].text == "No results!"
        else:
            self._click_element(self.RESULT_HEAD_CHECKBOX)
            self._click_element(self.PRODUCT_DELETE_BTN)
            self._handle_native_alert("Are you sure?")
            self._assert_alert_message()
