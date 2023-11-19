from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            logger("INFO", f"Element with locator:{locator[1]} found")
            return element
        except:
            print("Error: Element not found")
            logger("ERROR", f"Error: Element not found")
            exit(1)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _elementy_should_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("Element not visible but should be")
            exit(2)

    def _get_title(self):
        return self.driver.title

    def _fill_field(self, element, text):
        element.clear()
        element.send_keys(text)
        logger("INFO", "successfully added text to element")

    def _click_to_element(self, webElement):
        webElement.click()

    def _get_text(self, webElement):
        return webElement.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

