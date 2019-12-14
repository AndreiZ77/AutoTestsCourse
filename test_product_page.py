# pytest -v --tb=line test_product_page.py
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

#@pytest.mark.parametrize('offer_num', range(10))

@pytest.mark.parametrize('offer_num', [0])  # , 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(self, browser, offer_num):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


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


def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # Гость открывает страницу товара
    # Переходит в корзину по кнопке в шапке
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    # запуск тестирования страницы basket_page
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_main_elements()
    basket_page.should_be_basket_empty_elements()
    basket_page.should_be_basket_url()


@pytest.mark.login
class TestLoginFromProductPage():
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title = "Best book created by robot")
    #     # создаем по апи
    #     self.link = self.product.link
    #     yield
    #     # после этого ключевого слова начинается teardown
    #     # выполнится после каждого теста в классе
    #     # удаляем те данные, которые мы создали
    #     self.product.delete()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

class TestUserAddToBasketFromProductPage():
#Добавьте в класс фикстуру setup. В этой функции нужно:
# открыть страницу регистрации
# зарегистрировать нового пользователя
# проверить, что пользователь залогинен
    @pytest.mark.parametrize('offer_num', [0])  # , 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_user_can_add_product_to_basket(self, browser, offer_num):
        link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}")
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()


    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_main_elements()
        basket_page.should_be_basket_empty_elements()
        basket_page.should_be_basket_url()