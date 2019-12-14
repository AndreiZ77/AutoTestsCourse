from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес страницы логина
        url = self.browser.current_url
        assert "login" in url , f"Login URL:'{url}' is not contains 'login'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_REMIND), "Login remind-link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit-button is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration form email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD_1), "Registration form password_1 is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD_2), "Registration form password_2 is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_SUBMIT), "Registration form submit-button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()
        with open('testusers.txt', 'a') as f:
            f.write(f"{email}:{password}\n")
