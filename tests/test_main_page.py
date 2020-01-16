from pages.main_page import MainPage
import time


link ='http://selenium1py.pythonanywhere.com/'

def go_to_login_page(browser):
    page = MainPage(browser, link)

class TestLogin(object):

    def test_is_button_exist(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



