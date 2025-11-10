from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Util.Util import BrowserUtil


class checkout_and_purchase(BrowserUtil):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country_input = (By.ID, "country")
        self.country_select = (By.LINK_TEXT, 'India')
        self.checkbox_select = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        self.purchase_button = (By.XPATH, "//input[@type = 'submit']")
        self.alert_msg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def checkout(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.checkout_button)).click()


    def enter_delivery_address(self,countryname):
        self.driver.find_element(*self.country_input).send_keys(countryname)
        WebDriverWait(self.driver, 12).until(expected_conditions.visibility_of_element_located(self.country_select)).click()
        self.driver.find_element(*self.checkbox_select).click()
        self.driver.find_element(*self.purchase_button).click()


    def validate_Order(self):
        success_text = self.driver.find_element(*self.alert_msg).text
        assert "Success!" in success_text

