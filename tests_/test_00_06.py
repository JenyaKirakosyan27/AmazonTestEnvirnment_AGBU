import unittest
from selenium import webdriver
from time import sleep
from pages_.navigationBarPage import NavigationBar
from pages_.loginPage import LogInPage
from pages_.cartPage import CartPage
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver


class ProductDeletionTest(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPageObj = LogInPage(self.driver)
        self.loginPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_fild("//eva[@tsaturyan]")
        sleep(10)  # Added sleep time to avoid captcha from amazon
        self.loginPageObj.click_to_signin_button()
    def test_empty_or_not_cart_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()

        cartPageObj = CartPage(self.driver)
        cartPageObj.validate_empty_or_not_cart_page()

    def test_for_first_product_deletion(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()

        cartPageObj = CartPage(self.driver)
        cartElementBeforeDeletion = cartPageObj.get_cart_count_element()
        cartPageObj.delete_first_product_from_cart()
        cartElementAfterDeletion = cartPageObj.get_cart_count_element()
        self.assertEqual(cartElementBeforeDeletion - 1, cartElementAfterDeletion)

    def test_delete_all_products_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()

        cartPageObj = CartPage(self.driver)
        cartCurrentElement = cartPageObj.get_cart_count_element()
        cartPageObj.delete_all_product_from_cart()
        self.assertEqual(cartCurrentElement, 0, "The Cart Is Empty")

    def tearDown(self):
        self.driver.close()
