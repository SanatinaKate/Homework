import pytest
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    timeout = request.config.getoption("--timeout")

    if browser == "chrome":
        service = Service(executable_path=f"{ROOT}/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{ROOT}/geckodriver.exe")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{ROOT}/operadriver.exe")
    else:
        raise Exception("Browser is not supported")

    request.addfinalizer(driver.quit)

    def open_url(added_path=""):
        return driver.get(url=base_url + added_path)

    driver.open = open_url
    driver.timeout = timeout
    driver.maximize_window()

    return driver
