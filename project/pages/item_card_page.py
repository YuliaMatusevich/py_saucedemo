from project.pages.base_page import BasePage
from project.locators.item_card_page_locators import ItemCardPageLocators
from project.pages.cart_page import CartPage


class ItemCardPage(BasePage):
    locators = ItemCardPageLocators()

    def get_item_name(self):
        return self.find(self.locators.ITEM_NAME).text

    def click_add_to_cart(self):
        self.find(self.locators.ADD_BUTTON_ITEM_CARD).click()
        return self

    def click_cart_icon(self):
        self.find(self.locators.CART_ICON).click()
        return CartPage(driver=self.driver)


