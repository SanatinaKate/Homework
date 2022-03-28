from Homework_06.page_objects.AdminPage import AdminPage
from Homework_06.page_objects.CatalogPage import CatalogPage
from Homework_06.page_objects.MainPage import MainPage
from Homework_06.page_objects.ProductPage import ProductPage
from Homework_06.page_objects.RegistrationPage import RegistrationPage


def test_main_page(browser):
    browser.open()
    main_page = MainPage(browser)

    main_page._check_element_visible(MainPage.LOGO)

    main_page._check_element_clickable(MainPage.SEARCH_BTN)

    main_page._click_element(MainPage.CART_BTN)
    main_page._check_element_text(MainPage.CART_MENU, "Your shopping cart is empty!")

    main_page._check_element_visible(MainPage.CONTENT)
    assert main_page._get_values(MainPage.FEATURED, MainPage.FEATURED_NAME) == MainPage.EXPECTED_NAMES


def test_cameras_catalog_page(browser):
    browser.open("/index.php?route=product/category&path=33")
    catalog_page = CatalogPage(browser)

    catalog_page._check_element_visible(CatalogPage.CAMERAS_TITLE)
    catalog_page._check_element_text(CatalogPage.CAMERAS_TITLE, "Cameras")

    catalog_page._check_element_clickable(CatalogPage.LIST_VIEW)
    catalog_page._check_element_clickable(CatalogPage.GRID_VIEW)

    catalog_page._check_element_clickable(CatalogPage.SORT_MENU)
    assert catalog_page._get_menu_option(CatalogPage.SORT_MENU, 0) == "Default"

    catalog_page._check_element_clickable(CatalogPage.SHOW_MENU)
    assert catalog_page._get_menu_options(CatalogPage.SHOW_MENU) == CatalogPage.EXPECTED_LIMITS

    catalog_page._check_element_visible(CatalogPage.CONTENT)
    assert catalog_page._get_values(CatalogPage.PRODUCTS, CatalogPage.PRODUCT_NAME) == CatalogPage.EXPECTED_NAMES


def test_canon_camera_page(browser):
    browser.open("/index.php?route=product/product&path=33&product_id=30")
    product_page = ProductPage(browser)

    product_page._check_element_clickable(ProductPage.IMAGE)
    product_page._check_element_clickable(ProductPage.DESCRIPTION)
    product_page._check_element_clickable(ProductPage.REVIEWS)

    product_page._check_element_visible(ProductPage.CONTENT)
    product_page._check_element_text(ProductPage.PRODUCT_TITLE, "Canon EOS 5D")
    for currency in ProductPage.CURRENCIES:
        product_page._switch_currency(currency)
        assert product_page._get_currency == currency
        product_page._check_element_text(ProductPage.PRODUCT_PRICE, ProductPage.EXPECTED_PRICE[currency])

    product_page._check_element_clickable(ProductPage.ADD_TO_CART_BTN)


def test_admin_page(browser):
    browser.open("/admin")
    admin_page = AdminPage(browser)

    admin_page._check_element_visible(AdminPage.LOGO)
    admin_page._check_element_text(AdminPage.LOGIN_PANEL_TITLE, "Please enter your login details.")
    admin_page._check_element_text(AdminPage.USERNAME_TITLE, "Username")
    admin_page._check_element_text(AdminPage.PASSWORD_TITLE, "Password")

    admin_page._login(AdminPage.ADMIN_USERNAME, AdminPage.ADMIN_PASSWORD)
    admin_page._add_product(AdminPage.PRODUCT)
    admin_page._delete_product(AdminPage.PRODUCT)


def test_registration_page(browser):
    browser.open("/index.php?route=account/register")
    registration_page = RegistrationPage(browser)

    registration_page._check_element_text(RegistrationPage.CONTENT_TITLE, "Register Account")
    registration_page._check_element_text(RegistrationPage.PERSONAL_DETAILS_TITLE, "Your Personal Details")
    registration_page._check_element_text(RegistrationPage.FIRST_NAME_LABEL, "First Name")
    registration_page._check_element_text(RegistrationPage.LAST_NAME_LABEL, "Last Name")
    registration_page._check_element_text(RegistrationPage.EMAIL_LABEL, "E-Mail")
    registration_page._check_element_text(RegistrationPage.TELEPHONE_LABEL, "Telephone")
    registration_page._check_element_text(RegistrationPage.PASSWORD_TITLE, "Your Password")
    registration_page._check_element_text(RegistrationPage.PASSWORD_LABEL, "Password")
    registration_page._check_element_text(RegistrationPage.CONFIRM_LABEL, "Password Confirm")

    registration_page._register_account(RegistrationPage.USER)
    registration_page._logout()
    