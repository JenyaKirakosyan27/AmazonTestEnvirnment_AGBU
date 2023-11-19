from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value = 'Delete'])[1]")
        self.__firstProductSaveForLaterButtonLocator = (By.XPATH, "(//input[@value='Save for later'])[1]")
        self.__allItemsDeselectFromCartLocator = (By.ID, "deselect-all")
        self.__cartCountLocator = (By.ID, "nav-cart-count")

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click_to_element(firstProductDeleteButtonElement)

    def save_for_later_first_product_from_cart(self):
        firstProductSaveForLaterButtonElement = self._find_element(self.__firstProductSaveForLaterButtonLocator)
        self._click_to_element(firstProductSaveForLaterButtonElement)

    def deselect_all_items_from_cart(self):
        allItemsDeselectFromCartElement = self._find_element(self.__allItemsDeselectFromCartLocator)
        self._click_to_element(allItemsDeselectFromCartElement)

    def validate_empty_or_not_cart_page(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        if int(self._get_text(cartCountElement)) == 0:
            print("Warning! The Cart Is Empty")
        if int(self._get_text(cartCountElement)) != 0:
            print("Warning! The Cart Is Empty")

    def get_cart_count_element(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_text(cartCountElement))

    def delete_all_product_from_cart(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        while int(self._get_text(cartCountElement)) != 0:
            firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
            self._click_to_element(firstProductDeleteButtonElement)
