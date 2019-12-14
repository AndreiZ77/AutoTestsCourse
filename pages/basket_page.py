from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        # проверка на корректный url адрес страницы
        url = self.browser.current_url
        assert "basket" in url, f"Login URL:'{url}' is not contains 'basket'"

    def should_be_basket_main_elements(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HOME), \
            "Link to home page is not presented"

    def should_be_basket_empty_elements(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "'Basket is empty' message is not presented"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_CONTINUE), \
            "'Continue shopping' link is not presented in basket"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), \
            "'Products list' is presented in empty basket"

    def should_be_basket_is_not_empty_elements(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "'Basket is empty' message in is not empty basket"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_CONTINUE), \
            "'Continue shopping' link in is not empty basket"
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), \
            "'Products list' is not presented in basket"
