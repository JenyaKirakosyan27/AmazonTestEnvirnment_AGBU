import unittest
from selenium import webdriver
from pages_.loginPage import LogInPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LogInTest(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_logIn(self):
        #test Amazon Log in with valid data
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_fild("//eva[@ts]")
        sleep(5) # Added sleep time to avoid captcha from amazon
        logInPageObj.click_to_signin_button()
        self.assertEqual(self.driver.title, "Amazon Sign-In")
        
    def test_logIn_with_invalid_password(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_fild("WrongPassword")
        sleep(5) # Added sleep time to avoid captcha from amazon
        logInPageObj.click_to_signin_button()
        logInPageObj.validate_incorrect_password_alert()

    def test_logIn_with_invalid_email_address_or_mobile_phone_number(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field("jenyakirakosyan2@gmail.com")
        logInPageObj.click_to_continue_button()
        logInPageObj.validate_incorrect_email_address_or_mobile_phone_number_alert()

    def tearDown(self):
        self.driver.close()


