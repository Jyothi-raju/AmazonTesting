from selenium.webdriver.common.by import By

from Util.Util import BrowserUtil
from .checkout_and_purchase import checkout_and_purchase


class ShopPage(BrowserUtil):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_button = (By.XPATH, "//a[text() = 'Shop']")
        self.product_cards = (By.CSS_SELECTOR, ".card.h-100")
        self.cart_button = (By.XPATH, "//ul/li[@class = 'nav-item active']")

    def add_items_to_cart(self,product_name):
        self.driver.find_element(*self.shop_button).click()
        phones_list = self.driver.find_elements(*self.product_cards)
        # selecting blackberry product
        for phone in phones_list:
            productname = phone.find_element(By.XPATH, "div/h4[@class= 'card-title']").text
            if productname == product_name:
                self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()
                break

    def goToCart(self):
        self.driver.find_element(*self.cart_button).click()
        checkoutpage = checkout_and_purchase(self.driver)
        return checkoutpage