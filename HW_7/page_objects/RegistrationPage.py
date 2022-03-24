from selenium.webdriver.common.by import By
from time import time
from Homework_07.page_objects.BasePage import BasePage


class RegistrationPage(BasePage):

    # Locators
    CONTENT_TITLE = (By.CSS_SELECTOR, "#content h1")
    PERSONAL_DETAILS_TITLE = (By.CSS_SELECTOR, "#account legend")
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, "#account div:nth-child(3) label")
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_LABEL = (By.CSS_SELECTOR, "#account div:nth-child(4) label")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_LABEL = (By.CSS_SELECTOR, "#account div:nth-child(5) label")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_LABEL = (By.CSS_SELECTOR, "#account div:nth-child(6) label")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_TITLE = (By.CSS_SELECTOR, "#content fieldset:nth-child(2) legend")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "#content fieldset:nth-child(2) div:nth-child(2) label")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_LABEL = (By.CSS_SELECTOR, "#content fieldset:nth-child(2) div:nth-child(3) label")
    CONFIRM_INPUT = (By.ID, "input-confirm")
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input[type='submit']")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".buttons .pull-right")
    OPTIONS_LIST = (By.CSS_SELECTOR, "#column-right div[class='list-group']")
    LOGOUT = (By.CSS_SELECTOR, "#column-right div a:nth-child(13)")

    def _register_account(self, user: dict):
        time_id = str(int(time()))
        self._fill_input(self.FIRST_NAME_INPUT, f"{user['First Name']}-{time_id}")
        self._fill_input(self.LAST_NAME_INPUT, f"{user['Last Name']}-{time_id}")
        e_mail = user['E-Mail'].split("@")
        self._fill_input(self.EMAIL_INPUT, f"{e_mail[0]}-{time_id}@{e_mail[1]}")
        self._fill_input(self.TELEPHONE_INPUT, user['Telephone'])
        self._fill_input(self.PASSWORD_INPUT, user['Password'])
        self._fill_input(self.CONFIRM_INPUT, user['Password'])
        self._click_element(self.POLICY_CHECKBOX)
        self._click_element(self.SUBMIT_BTN)
        self._check_element_text(self.CONTENT_TITLE, "Your Account Has Been Created!")
        self._click_element(self.CONTINUE_BTN)
        self._check_element_visible(self.OPTIONS_LIST)

    def _logout(self):
        self._click_element(self.LOGOUT)
        self._check_element_text(self.CONTENT_TITLE, "Account Logout")
        self._click_element(self.CONTINUE_BTN)
