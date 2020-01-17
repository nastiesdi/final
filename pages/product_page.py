from pages.main_page import MainPage

from .locators import ProductPageLocators
from .const import PageText


class ProductPage(MainPage):

    def add_thing_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_name_from_message(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_price_from_message(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

    def get_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADDING_MASSAGES).text

    def name_should_be_in_message(self):
        name = self.get_product_name_from_message()
        print(f' exp: {name}, actual: {self.get_product_name()}')
        assert name == f'{self.get_product_name()} был добавлен в вашу корзину.', 'Name product is not in message'

    def price_should_be_in_message(self):
        price = self.get_product_price_from_message()
        print(f' exp: {price}, actual: {self.get_product_price()}')
        assert price == f'Стоимость корзины теперь составляет {self.get_product_price()}', 'Price product is not in message'

    def text_message_should_be_equivalent(self):
        text_message = PageText.PRODUCT_WAS_ADDED
        print(f' exp: {text_message}, actual: {self.get_message()}')
        assert text_message in self.get_message(), 'Text message is not right'



    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDING_MASSAGES), \
    #        "Success message is presented, but should not be"
    #
    # def should_not_displaied_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDING_MASSAGES),'Success message is presented"'
    #
    # def should_not_disappered(self):
    #    assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDING_MASSAGES),'Success message is presented"'