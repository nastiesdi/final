from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
