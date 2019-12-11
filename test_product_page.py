# pytest -v --tb=line test_product_page.py
from .pages.product_page import ProductPage
import pytest
import time

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

#@pytest.mark.parametrize('offer_num', range(10))
@pytest.mark.parametrize('offer_num', [0])#, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

@pytest.mark.parametrize('offer_num', [0])
@pytest.mark.xfail(reason="test should be filed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, offer_num):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser, link, 1)
    page.open()
    page.product_can_be_add_to_cart()
    page.should_not_be_success_messages()

@pytest.mark.parametrize('offer_num', [0])
def test_guest_cant_see_success_message(browser, offer_num):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser, link, 1)
    page.open()
    page.should_not_be_success_messages()

@pytest.mark.parametrize('offer_num', [0])
@pytest.mark.xfail(reason="test should be filed")
def test_message_disappeared_after_adding_product_to_basket(browser, offer_num):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = ProductPage(browser, link, 1)
    page.open()
    page.product_can_be_add_to_cart()
    page.success_messages_is_disappeared()