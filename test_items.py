#There may be a link to another position from the catalog:
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"

# Add the product to the cart with different browser language.
def test_add_product_to_cart_with_set_language(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn.btn-primary.btn-add-to-basket")
    assert len(button) == 1, "Button to add product to cart not found!"