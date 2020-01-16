from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


link ='http://selenium1py.pythonanywhere.com/ru/accounts/login/'

def go_to_login_page(browser):
    page = MainPage(browser, link)

class TestLogin(object):

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_all_elements_on_login_page_exist(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()



