from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (
            "login" in self.browser.current_url
        ), "Login word is not present in current URL"
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM
        ).is_displayed(), "Login form is not displayed"
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM
        ).is_displayed(), "Register form is not displayed"
        assert True
