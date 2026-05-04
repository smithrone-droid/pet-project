from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        """Вернуть название товара из карточки продукта."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        """Вернуть цену товара из карточки продукта."""
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text.strip()

    def add_item_in_cart(self):
        """Нажать кнопку добавления в корзину для текущего товара."""
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def should_be_button_cart(self):
        """Проверить, что кнопка добавления в корзину есть на странице."""
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART
        ), "Add to cart button is not present"

    def should_be_product_name(self):
        """Проверить, что название товара отображается на странице."""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME
        ), "Product name is not present"

    def should_be_product_price(self):
        """Проверить, что цена товара отображается на странице."""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE
        ), "Product price is not present"

    def should_be_success_message(self):
        """Проверить, что после добавления товара появляется success-алерт."""
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not present after adding product to cart"

    def should_match_product_name_in_success_message(self):
        """Проверить, что имя товара в алерте совпадает с карточкой."""
        product_name = self.get_product_name()
        message_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text.strip()
        assert (
            product_name == message_name
        ), f"Expected product name '{product_name}', got '{message_name}'"

    def should_match_product_price_in_basket_total(self):
        """Проверить, что итог в корзине равен цене товара в карточке."""
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text.strip()
        assert (
            product_price == basket_total
        ), f"Expected basket total '{product_price}', got '{basket_total}'"
