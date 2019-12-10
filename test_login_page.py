# pytest -v --tb=line --language=en test_login_page.py
from .pages.login_page import LoginPage


def test_guest_can_login_or_register(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_page()      # выполняем проверку url, форм логина и регистрации

