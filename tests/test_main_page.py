from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


link ="http://selenium1py.pythonanywhere.com"

class TestLogin(object):

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_all_elements_on_login_page_exist(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()



