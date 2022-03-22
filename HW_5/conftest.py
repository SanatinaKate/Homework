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


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = Service(executable_path=f"{ROOT}/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{ROOT}/geckodriver.exe")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{ROOT}/operadriver.exe")
    else:
        raise Exception("Browser is not supported")
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
