from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


def test_main_page(browser, base_url):
    browser.get(url=base_url)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "logo")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "input-group-btn")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".col-sm-3 .btn"))).click()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".dropdown-menu.pull-right"), "Your shopping cart is empty!"))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "content")))
    for i in range(4):
        product = browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[i]
        product_name = product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
        assert product_name == ("MacBook", "iPhone", "Apple Cinema 30\"", "Canon EOS 5D")[i]


def test_cameras_catalog_page(browser, base_url):
    browser.get(url=base_url + f"/index.php?route=product/category&path=33")
    title = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-9 h2"))).text
    assert title == "Cameras"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "list-view")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "grid-view")))
    sort_by = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-sort")))
    assert Select(sort_by).first_selected_option.text == "Default"
    show = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-limit")))
    for i in range(5):
        assert Select(show).options[i].text == ("15", "25", "50", "75", "100")[i]
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "content")))
    for i in range(2):
        product = browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[i]
        product_name = product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
        assert product_name == ("Canon EOS 5D", "Nikon D300")[i]


def test_canon_camera_page(browser, base_url):
    browser.get(url=base_url + f"/index.php?route=product/product&path=33&product_id=30")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-8 img")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, "Description")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Reviews")))
    camera_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 h1"))).text
    assert camera_title == "Canon EOS 5D"
    camera_price = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 ul:nth-child(4) li:nth-child(2) h2"))).text
    assert camera_price == "$98.00"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "button-cart")))


def test_admin_page(browser, base_url):
    browser.get(url=base_url + f"/admin")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand img")))
    panel_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .panel-heading h1"))).text
    assert panel_title == "Please enter your login details."
    username_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .panel-body div:nth-child(1) label"))).text
    assert username_title == "Username"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-username")))
    password_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .panel-body div:nth-child(2) label"))).text
    assert password_title == "Password"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-password")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))


def test_registration_page(browser, base_url):
    browser.get(url=base_url + f"/index.php?route=account/register")
    title = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-9 h1"))).text
    assert title == "Register Account"
    personal_details_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#account legend"))).text
    assert personal_details_title == "Your Personal Details"
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#account div:nth-child(3) label"))).text
    assert label == "First Name"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-firstname")))
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#account div:nth-child(4) label"))).text
    assert label == "Last Name"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-lastname")))
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#account div:nth-child(5) label"))).text
    assert label == "E-Mail"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-email")))
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#account div:nth-child(6) label"))).text
    assert label == "Telephone"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-telephone")))
    password_title = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content fieldset:nth-child(2) legend"))).text
    assert password_title == "Your Password"
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content fieldset:nth-child(2) div:nth-child(2) label"))).text
    assert label == "Password"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-password")))
    label = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content fieldset:nth-child(2) div:nth-child(3) label"))).text
    assert label == "Password Confirm"
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "input-confirm")))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
