from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from json import load
import allure
import logging


class BasePage:

    def __init__(self, browser):
        self._browser = browser
        self._config_logger()

    def _config_logger(self):
        self._logger = logging.getLogger(name=type(self).__name__)
        self._handler = logging.FileHandler(filename=f"../logs/{self._browser.test_name}.log", encoding="utf-8")
        self._handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s"))
        self._logger.handlers.clear()
        self._logger.addHandler(hdlr=self._handler)
        self._logger.setLevel(level=self._browser.log_level)

    @allure.step("Get data from file {filename}")
    def _get_data_from_file(self, filename: str):
        self._logger.info(f"Get data from file {filename}")
        with open(filename, "r") as json_file:
            data = load(json_file)
        return data

    def _attach_screenshot(self):
        date_time = datetime.now().strftime("%d%m%Y_%H%M%S")
        screenshot_name = f"{date_time}_{self._browser.session_id}.png"
        with allure.step(f"Attach screenshot file {screenshot_name} to allure report"):
            self._logger.info(f"Attach screenshot file {screenshot_name} to allure report")
            allure.attach(
                attachment_type=allure.attachment_type.PNG,
                name=screenshot_name,
                body=self._browser.get_screenshot_as_png()
            )

    def _open(self, added_path: str = ""):
        url = self._browser.base_url + added_path
        with allure.step(f"Open URL {url}"):
            self._logger.info(f"Open URL {url}")
            self._browser.get(url=url)

    @allure.step("Check if element with locator {locator} is clickable")
    def _check_element_clickable(self, locator: tuple):
        self._logger.info(f"Check if element with locator {locator} is clickable")
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException:
            self._logger.error(f"Assertion Error: Can't find clickable element with locator {locator}")
            self._attach_screenshot()
            raise AssertionError(f"Can't find clickable element with locator {locator}")

    @allure.step("Check if element with locator {locator} is visible")
    def _check_element_visible(self, locator: tuple):
        self._logger.info(f"Check if element with locator {locator} is visible")
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            self._logger.error(f"Assertion Error: Can't find visible element with locator {locator}")
            self._attach_screenshot()
            raise AssertionError(f"Can't find visible element with locator {locator}")

    @allure.step("Check if text \"{text}\" is present in element with locator {locator}")
    def _check_element_text(self, locator: tuple, text: str):
        self._logger.info(f"Check if text \"{text}\" is present in element with locator {locator}")
        try:
            return WebDriverWait(self._browser, self._browser.timeout).until(
                ec.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self._logger.error(f"Assertion Error: Can't find given text in element with locator {locator}")
            self._attach_screenshot()
            raise AssertionError(f"Can't find given text in element with locator {locator}")

    @allure.step("Check if text \"{text}\" is present in given WebElement")
    def _check_webelement_text(self, element: WebElement, text: str):
        self._logger.info(f"Check if text \"{text}\" is present in WebElement {element}")
        try:
            assert text in element.text
        except Exception:
            self._logger.error(f"Assertion Error: Can't find text \"{text}\" in given WebElement")
            self._attach_screenshot()
            raise AssertionError(f"Can't find text \"{text}\" in given WebElement")

    @allure.step("Check if one of text options {texts} is present in given WebElement")
    def _check_webelement_text_options(self, element: WebElement, texts: tuple):
        self._logger.info(f"Check if one of text options {texts} is present in WebElement {element}")
        flag = False
        for text in texts:
            flag = flag or (text in element.text)
        try:
            assert flag
        except Exception:
            self._logger.error(f"Assertion Error: Can't find none of text options {texts} in given WebElement")
            self._attach_screenshot()
            raise AssertionError(f"Can't find none of text options {texts} in given WebElement")

    @allure.step("Click element with locator {locator}")
    def _click_element(self, locator: tuple):
        self._logger.info(f"Click element with locator {locator}")
        self._check_element_clickable(locator).click()

    @allure.step("Find elements with locator {locator}")
    def _find_elements(self, locator: tuple):
        self._logger.info(f"Find elements with locator {locator}")
        try:
            return self._browser.find_elements(*locator)
        except NoSuchElementException:
            self._logger.error(f"Assertion Error: Can't find elements with locator {locator}")
            self._attach_screenshot()
            raise AssertionError(f"Can't find elements with locator {locator}")

    @allure.step("Find element with locator {locator}")
    def _find_element(self, locator: tuple):
        self._logger.info(f"Find element with locator {locator}")
        try:
            return self._browser.find_element(*locator)
        except NoSuchElementException:
            self._logger.error(f"Assertion Error: Can't find element with locator {locator}")
            self._attach_screenshot()
            raise AssertionError(f"Can't find element with locator {locator}")

    @allure.step("Find element with locator {locator} from given base WebElement")
    def _find_element_from_base(self, base: WebElement, locator: tuple):
        self._logger.info(f"Find element with locator {locator} from base {base}")
        try:
            return base.find_element(*locator)
        except NoSuchElementException:
            self._logger.error(f"Assertion Error: Can't find element with locator {locator} from given base")
            self._attach_screenshot()
            raise AssertionError(f"Can't find element with locator {locator} from given base")

    @allure.step("Get list of elements with locator {target_locator} from base with locator {base_locator}")
    def _get_elements_list(self, base_locator: tuple, target_locator: tuple):
        self._logger.info(f"Get list of elements with locator {target_locator} from base with locator {base_locator}")
        elements = []
        base_elements = self._find_elements(base_locator)
        for base_element in base_elements:
            element = self._find_element_from_base(base_element, target_locator)
            elements.append(element)
        return elements

    @allure.step("Enter value \"{value}\" into input with locator {input_locator}")
    def _fill_input(self, input_locator: tuple, value: str):
        self._logger.info(f"Enter value \"{value}\" into input with locator {input_locator}")
        input_to_fill = self._check_element_clickable(input_locator)
        input_to_fill.click()
        input_to_fill.clear()
        input_to_fill.send_keys(value)

    @allure.step("Accept native browser alert")
    def _accept_native_alert(self):
        try:
            alert = WebDriverWait(self._browser, self._browser.timeout).until(ec.alert_is_present())
        except TimeoutException:
            self._logger.error(f"Assertion Error: Can't find native browser alert")
            self._attach_screenshot()
            raise AssertionError("Can't find native browser alert")
        else:
            self._logger.info("Accept native browser alert")
            alert.accept()
