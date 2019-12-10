from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#login_form #id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login_form #id_login-password")
    LOGIN_LINK_REMIND = (By.CSS_SELECTOR, "#login_form #id_login-redirect_url")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form .btn.btn-lg.btn-primary")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REG_PASSWORD_1 = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")
