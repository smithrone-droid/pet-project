from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

# pytest -v --tb=line --language=ru test_product_page.py
# pytest -v -s --setup-show --tb=line --language=ru test_product_page.py

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_should_see_product_card_data(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.should_be_product_price()
    page.should_be_button_cart()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_match_product_name_in_success_message()
    page.should_match_product_price_in_basket_total()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_cart()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message is present, but should not be"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message is present, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_cart()
    assert page.is_disappeared(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message did not disappear"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

