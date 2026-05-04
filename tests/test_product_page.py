from pages.product_page import ProductPage


# pytest -v --tb=line --language=ru test_product_page.py
# pytest -v -s --setup-show --tb=line --language=ru test_product_page.py

def test_guest_should_see_product_card_data(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.should_be_product_price()
    page.should_be_button_cart()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_match_product_name_in_success_message()
    page.should_match_product_price_in_basket_total()
