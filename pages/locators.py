from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_EMPTY_CONTINUE = (By.CSS_SELECTOR, "#content_inner > p > a")
    BASKET_HOME = (By.CSS_SELECTOR, ".page_inner .breadcrumb a")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, "#content_inner .basket-title.hidden-xs .row")


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


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_AVAILABLE = (By.CSS_SELECTOR, ".instock.availability .icon-ok")
    PRODUCT_REVIEW = (By.CSS_SELECTOR, ".product_main #write_review")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".carousel-inner .item.active img")
    PRODUCT_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR,
                            "#messages .alert-noicon.alert-success.fade.in strong:nth-child(1)")
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR,
                             "#messages .alert-noicon.alert-info.fade.in strong")
