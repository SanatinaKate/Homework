from Homework_07.page_objects.AdminPage import AdminPage
from Homework_07.page_objects.CatalogPage import CatalogPage
from Homework_07.page_objects.MainPage import MainPage
from Homework_07.page_objects.ProductPage import ProductPage
from Homework_07.page_objects.RegistrationPage import RegistrationPage
import allure


@allure.title("Tests for Main Page")
def test_main_page(browser):
    main_page = MainPage(browser)

    with allure.step("Open Main Page"):
        main_page._open()

    with allure.step("Check Logo"):
        main_page._check_element_visible(MainPage.LOGO)

    with allure.step("Check Search Button"):
        main_page._check_element_clickable(MainPage.SEARCH_BTN)

    with allure.step("Check Shopping Cart"):
        main_page._click_element(MainPage.CART_BTN)
        main_page._check_element_text(MainPage.CART_MENU, "Your shopping cart is empty!")

    with allure.step("Check Featured Products"):
        main_page._check_element_visible(MainPage.CONTENT)
        elements = main_page._get_elements_list(MainPage.FEATURED, MainPage.FEATURED_NAME)
        for i in range(len(elements)):
            main_page._check_webelement_text(elements[i], MainPage.EXPECTED_NAMES[i])


@allure.title("Tests for Cameras Catalog Page")
def test_cameras_catalog_page(browser):
    catalog_page = CatalogPage(browser)

    with allure.step("Open Cameras Catalog Page"):
        catalog_page._open("/index.php?route=product/category&path=33")

    with allure.step("Check Title"):
        catalog_page._check_element_visible(CatalogPage.CAMERAS_TITLE)
        catalog_page._check_element_text(CatalogPage.CAMERAS_TITLE, "Cameras")

    with allure.step("Check Views"):
        catalog_page._check_element_clickable(CatalogPage.LIST_VIEW)
        catalog_page._check_element_clickable(CatalogPage.GRID_VIEW)

    with allure.step("Check Sort Menu"):
        catalog_page._check_element_clickable(CatalogPage.SORT_MENU)
        elements = catalog_page._find_elements(CatalogPage.SORT_MENU)
        catalog_page._check_webelement_text(elements[0], "Default")

    with allure.step("Check Show Menu"):
        catalog_page._check_element_clickable(CatalogPage.SHOW_MENU)
        elements = catalog_page._find_elements(CatalogPage.SHOW_MENU)
        for i in range(len(elements)):
            catalog_page._check_webelement_text(elements[i], CatalogPage.EXPECTED_LIMITS[i])

    with allure.step("Check Products"):
        catalog_page._check_element_visible(CatalogPage.CONTENT)
        elements = catalog_page._get_elements_list(CatalogPage.PRODUCTS, CatalogPage.PRODUCT_NAME)
        for i in range(len(elements)):
            catalog_page._check_webelement_text(elements[i], CatalogPage.EXPECTED_NAMES[i])


@allure.title("Tests for Canon Camera Page")
def test_canon_camera_page(browser):
    product_page = ProductPage(browser)

    with allure.step("Open Canon Camera Page"):
        product_page._open("/index.php?route=product/product&path=33&product_id=30")

    with allure.step("Check Camera Image"):
        product_page._check_element_clickable(ProductPage.IMAGE)

    with allure.step("Check Camera Description"):
        product_page._check_element_clickable(ProductPage.DESCRIPTION)

    with allure.step("Check Camera Reviews"):
        product_page._check_element_clickable(ProductPage.REVIEWS)

    with allure.step("Check Camera Name"):
        product_page._check_element_visible(ProductPage.CONTENT)
        product_page._check_element_text(ProductPage.PRODUCT_TITLE, "Canon EOS 5D")

    with allure.step("Check Currencies Switching and Camera Price"):
        for currency in ProductPage.CURRENCIES:
            product_page._switch_currency(currency)
            product_page._check_element_text(ProductPage.CURRENCY_ACTIVE, currency)
            product_page._check_element_text(ProductPage.PRODUCT_PRICE, ProductPage.EXPECTED_PRICE[currency])

    with allure.step("Check 'Add to Cart' Button"):
        product_page._check_element_clickable(ProductPage.ADD_TO_CART_BTN)


@allure.title("Tests for Admin Page")
def test_admin_page(browser):
    admin_page = AdminPage(browser)

    with allure.step("Open Admin Page"):
        admin_page._open("/admin")

    with allure.step("Check Logo"):
        admin_page._check_element_visible(AdminPage.LOGO)

    with allure.step("Check Titles in Login Form"):
        admin_page._check_element_text(AdminPage.LOGIN_PANEL_TITLE, "Please enter your login details.")
        admin_page._check_element_text(AdminPage.USERNAME_TITLE, "Username")
        admin_page._check_element_text(AdminPage.PASSWORD_TITLE, "Password")

    with allure.step("Check Login Procedure"):
        credentials = admin_page._get_data_from_file("../data_files/credentials.json")
        admin_page._login(credentials)

    with allure.step("Check Product Addition"):
        product = admin_page._get_data_from_file("../data_files/product.json")
        admin_page._add_product(product)

    with allure.step("Check Product Deletion"):
        admin_page._delete_product(product)


@allure.title("Tests for Registration Page")
def test_registration_page(browser):
    registration_page = RegistrationPage(browser)

    with allure.step("Open Registration Page"):
        registration_page._open("/index.php?route=account/register")

    with allure.step("Check Inputs' Labels"):
        registration_page._check_element_text(RegistrationPage.CONTENT_TITLE, "Register Account")
        registration_page._check_element_text(RegistrationPage.PERSONAL_DETAILS_TITLE, "Your Personal Details")
        registration_page._check_element_text(RegistrationPage.FIRST_NAME_LABEL, "First Name")
        registration_page._check_element_text(RegistrationPage.LAST_NAME_LABEL, "Last Name")
        registration_page._check_element_text(RegistrationPage.EMAIL_LABEL, "E-Mail")
        registration_page._check_element_text(RegistrationPage.TELEPHONE_LABEL, "Telephone")
        registration_page._check_element_text(RegistrationPage.PASSWORD_TITLE, "Your Password")
        registration_page._check_element_text(RegistrationPage.PASSWORD_LABEL, "Password")
        registration_page._check_element_text(RegistrationPage.CONFIRM_LABEL, "Password Confirm")

    with allure.step("Check Account Registration Procedure"):
        user = registration_page._get_data_from_file("../data_files/user.json")
        registration_page._register_account(user)

    with allure.step("Check Account Logout Procedure"):
        registration_page._logout()
