from os import makedirs, path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options
import logging
import pytest


ROOT = path.expanduser("~/OTUS/drivers")


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox", "opera"], help="Browser to run"
    )
    parser.addoption(
        "--url", default="https://demo.opencart.com", help="URL to open"
    )
    parser.addoption(
        "--timeout", type=int, default=5, help="Timeout to wait elements"
    )
    parser.addoption(
        "--log_level", default="INFO", help="Level for logging"
    )
    parser.addoption(
        "--executor", default="local", help="Executor for tests"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    item.status = report.outcome.upper()


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    timeout = request.config.getoption("--timeout")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")

    makedirs(name="../logs", exist_ok=True)
    test_name = request.node.name
    handler = logging.FileHandler(filename=f"../logs/{test_name}.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s"))
    logger = logging.getLogger(name="Browser")
    logger.handlers.clear()
    logger.addHandler(hdlr=handler)
    logger.setLevel(level=log_level)
    logger.info(f"===== Test {test_name} is started =====")

    if browser in ["chrome", "firefox", "opera"]:
        driver = None
        if executor == "local":
            if browser == "chrome":
                service = Service(executable_path=f"{ROOT}/chromedriver.exe")
                driver = webdriver.Chrome(service=service)
            elif browser == "firefox":
                driver = webdriver.Firefox(executable_path=f"{ROOT}/geckodriver.exe")
            elif browser == "opera":
                driver = webdriver.Opera(executable_path=f"{ROOT}/operadriver.exe")
        else:
            options = None
            if browser == "chrome":
                options = webdriver.ChromeOptions()
            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
            elif browser == "opera":
                options = Options()
            driver = webdriver.Remote(
                command_executor=f"http://{executor}:4444/wd/hub",
                options=options
            )
    else:
        raise Exception("Browser is not supported")

    def finalizer():
        logger.info(f"===== Test {test_name} is finished with status {request.node.status} =====")
        driver.quit()

    request.addfinalizer(finalizer)

    driver.base_url = base_url
    driver.log_level = log_level
    driver.test_name = test_name
    driver.timeout = timeout
    driver.maximize_window()

    return driver
