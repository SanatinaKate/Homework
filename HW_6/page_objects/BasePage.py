from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, browser):
        self._browser = browser

    def _check_element_clickable(self, locator: tuple):
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find clickable element by locator: {locator}")

    def _check_element_visible(self, locator: tuple):
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find visible element by locator: {locator}")

    def _check_element_text(self, locator: tuple, text: str):
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError(f"Can't find given text in element by locator: {locator}")

    def _click_element(self, locator: tuple):
        self._check_element_clickable(locator).click()

    def _find_elements(self, locator: tuple):
        try:
            return self._browser.find_elements(*locator)
        except NoSuchElementException:
            raise AssertionError(f"Can't find elements by locator: {locator}")

    def _find_element(self, locator: tuple):
        try:
            return self._browser.find_element(*locator)
        except NoSuchElementException:
            raise AssertionError(f"Can't find element by locator: {locator}")

    @staticmethod
    def _find_element_from_base(base: WebElement, locator: tuple):
        try:
            return base.find_element(*locator)
        except NoSuchElementException:
            raise AssertionError(f"Can't find element from given base by locator: {locator}")

    def _get_values(self, elements_locator: tuple, value_locator: tuple):
        values = []
        elements = self._find_elements(elements_locator)
        for element in elements:
            value = self._find_element_from_base(element, value_locator).text
            values.append(value)
        return values

    def _fill_input(self, input_locator: tuple, value: str):
        input_to_fill = self._check_element_clickable(input_locator)
        input_to_fill.click()
        input_to_fill.clear()
        input_to_fill.send_keys(value)

    def _handle_native_alert(self, text: str):
        alert = Alert(self._browser)
        if alert.text == text:
            alert.accept()
        else:
            alert.dismiss()
