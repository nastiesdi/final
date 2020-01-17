from pages.main_page import MainPage
from .locators import ProductPageLocators, BasketPageLocators
from .const import PageText


class BasketPage(MainPage):

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), 'Some product in basket'
        assert PageText.BASKET_IS_EMPTY in self.browser.find_element(*BasketPageLocators.CONTENT).text, \
            'Text that basket is empty is not displayed'
