from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_elements()
        self.product_can_be_add_to_cart()
        self.should_be_success_messages()

    def should_be_elements(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "Product picture is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_AVAILABLE), "Product is not available"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_REVIEW), "Product review button is not presented"

    def should_not_be_success_messages(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE_NAME), \
            "Success message 'product add basket' is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE_PRICE), \
            "Success message 'product price add' is presented, but should not be"

    def success_messages_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_MESSAGE_NAME), \
            "Success message 'product add basket' is not disappeared"
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_MESSAGE_PRICE), \
            "Success message 'product price add' is not disappeared"

    def product_can_be_add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()  # return code

    def should_be_success_messages(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_MESSAGE_NAME), "Message 'product add to basket' is not presented"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_MESSAGE_PRICE), "Message with price is not presented"
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        prod_message_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_NAME).text
        prod_message_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_PRICE).text

        assert prod_name == prod_message_name, \
            f"The product name: '{prod_message_name}' in the basket, does not match '{prod_name}'"
        assert prod_price == prod_message_price, \
            f"The product price: [{prod_message_price}] in the basket, does not match [{prod_price}]"
