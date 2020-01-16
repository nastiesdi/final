
import time


link ='http://selenium1py.pythonanywhere.com/'


class TestLogin(object):
    def test_is_button_exist(self, browser):
        browser.get(link)
        # browser.find_element_by_css_selector("#login_link")
        # browser.get(link)
        login_link = browser.find_element_by_css_selector("#login_link")
        time.sleep(5)
        login_link.click()


