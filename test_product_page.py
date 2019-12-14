# pytest -v --tb=line test_product_page.py
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

LINK_PARAM = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
LINK_LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.need_review
@pytest.mark.parametrize('offer_num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_num):
    page = ProductPage(browser, LINK_PARAM + str(offer_num))
    page.open()
    page.should_be_product_page()


@pytest.mark.parametrize('offer_num', [0, 1, 2])
def test_guest_cant_see_success_message(browser, offer_num):
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser, LINK_PARAM + str(offer_num))
    page.open()
    page.should_not_be_success_messages()


@pytest.mark.parametrize('offer_num', [0, 1, 2])
@pytest.mark.xfail(reason="test should be filed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, offer_num):
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser, LINK_PARAM + str(offer_num))
    page.open()
    page.product_can_be_add_to_cart()
    page.should_not_be_success_messages()


@pytest.mark.parametrize('offer_num', [0, 1, 2])
@pytest.mark.xfail(reason="test should be filed")
def test_message_disappeared_after_adding_product_to_basket(browser, offer_num):
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = ProductPage(browser, LINK_PARAM + str(offer_num))
    page.open()
    page.product_can_be_add_to_cart()
    page.success_messages_is_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_main_elements()
    basket_page.should_be_basket_empty_elements()
    basket_page.should_be_basket_url()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function")
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN)
        page.open()
        page.should_be_register_form()
        email = f"user{str(time.time()).split('.')[1]}@fakemail.com"
        password = "P@ssword!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_messages()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, LINK_PARAM + '3')
        page.open()
        page.should_be_product_page()
