import json

import pytest
from PageObjectModel.loginpage import LoginPage

with open("Data/test_data.json") as json_file:
    data = json.load(json_file)#here json format covert to python object
    test_list = data["data"]#list

@pytest.mark.parametrize("test_list_item",test_list)#test_list_item now in the 0th index
def test_e2e(BrowserSetup,test_list_item):
    driver = BrowserSetup
    loginpage = LoginPage(driver)
    print(loginpage.title())
    shoppage = loginpage.loginDetails(test_list_item["username"],test_list_item["password"])
    #clicking on shop
    shoppage.add_items_to_cart(test_list_item["productname"])
    checkoutpage = shoppage.goToCart()
    print(shoppage.title())
    #checoutpage,enter delivery address,success msg validation
    checkoutpage.checkout()
    print(checkoutpage.title())
    checkoutpage.enter_delivery_address(test_list_item["country"])
    checkoutpage.validate_Order()

