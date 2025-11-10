from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Util.Util import BrowserUtil
from .shoppage import ShopPage




class LoginPage(BrowserUtil):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #try to place all your locators in here
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.dropdown_select = (By.XPATH, "//select[@class = 'form-control']")
        self.checkbox_select = (By.ID, "terms")
        self.submit_button = (By.ID, "signInBtn")




    def loginDetails(self,username,password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        Select(self.driver.find_element(*self.dropdown_select)).select_by_visible_text("Student")
        self.driver.find_element(*self.checkbox_select).click()
        self.driver.find_element(*self.submit_button).click()
        shoppage = ShopPage(self.driver)
        return shoppage
