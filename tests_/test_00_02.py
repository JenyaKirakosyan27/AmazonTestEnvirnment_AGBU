import unittest
from selenium import webdriver
from pages_.loginPage import LogInPage
from pages_.navigationBarPage import NavigationBar
from pages_.serchResultPage import SearchResultPage
from pages_.productDetailsPage import ProductDetailsPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class ProductRelatedTest(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_search_product_and_add_to_cart(self):
        loginPageObj = LogInPage(self.driver)
        loginPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_fild("//eva[@tsaturyan]")
        sleep(10) # Added sleep time to avoid captcha from amazon
        loginPageObj.click_to_signin_button()

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("Dja 3 pro")
        navigationBarObj.click_to_search_button()

        searchResultPageObj = SearchResultPage(self.driver)
        searchResultPageObj.click_to_first_product()

        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_to_add_to_cart_button()
        self.assertEqual(self.driver.title, "Amazon.com Shopping Cart")

    def tearDown(self):
        self.driver.close()

