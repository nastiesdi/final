from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_PAGE = (By.CSS_SELECTOR, '.basket-mini .btn-group')


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_MAIL = (By.ID, "#id_login-username")
    LOGIN_PASSWORD = (By.ID, "#id_login-password")
    BUTTON_LOGIN = (By.NAME, 'login_submit')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_MAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.ID, "registration-password2")
    BUTTON_REGISTER = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_ADDING_MASSAGES = (By.ID, 'messages')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in div.alertinner')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in div.alertinner p')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')

class BasketPageLocators():
    PRODUCT = (By.CLASS_NAME, 'basket-items')
    CONTENT = (By.CSS_SELECTOR, '.page .page_inner')