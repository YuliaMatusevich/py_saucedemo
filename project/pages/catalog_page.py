from selenium.webdriver.common.by import By

from project.pages.base_page import BasePage
from project.locators.catalog_page_locators import CatalogPageLocators
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from project.pages.cart_page import CartPage
from project.pages.item_card_page import ItemCardPage


class CatalogPage(BasePage):
    locators = CatalogPageLocators()

    def add_sauce_labs_backpack(self):
        self.find(self.locators.ADD_BUTTON_SAUCE_LABS_BACKPACK).click()
        return CatalogPage(driver=self.driver)

    def delete_sauce_labs_backpack(self):
        self.find(self.locators.REMOVE_BUTTON_SAUCE_LABS_BACKPACK).click()
        return CatalogPage(driver=self.driver)

    def get_button_text_sauce_labs_backpack(self):
        return self.find(self.locators.ADD_BUTTON_SAUCE_LABS_BACKPACK).text

    def click_sauce_labs_backpack_item_name(self):
        self.find(self.locators.CATALOG_NAME_SAUCE_LABS_BACKPACK).click()
        return ItemCardPage(driver=self.driver)

    def click_cart_icon(self):
        self.find(self.locators.CART_ICON).click()
        return CartPage(driver=self.driver)
