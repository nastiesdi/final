from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"
        assert 'login' in self.browser.current_url, "URL dont't contains text 'login' "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"

    def register_new_user(self):
        print('aaaaa')
        self.browser.find_element(*LoginPageLocators.REGISTER_MAIL).sendKeys('nasty@mail.ru')
        print('ssssss')
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.sendKeys(123123)



