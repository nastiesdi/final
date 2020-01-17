from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage


import pytest
import time

# link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
class TestProduct(object):

    def test_all_elements_on_product_page_exist(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_thing_to_cart()
        page.solve_quiz_and_get_code()
        time.sleep(0)
        page.text_message_should_be_equivalent()
        page.name_should_be_in_message()
        page.price_should_be_in_message()

    def test_guest_should_see_login_link_on_product_page(swlf, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()

    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.add_thing_to_cart()
    #     time.sleep(1)
    #     page.should_not_displaied_success_message()

    # def test_guest_cant_see_success_message(self, browser, link):
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.should_not_displaied_success_message()
    #
    # def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.add_thing_to_cart()
    #     time.sleep(1)
    #     page.should_not_disappered()

