from project.pages.base_page import BasePage
from project.locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    locators = CartPageLocators()

    def get_cart_list_items(self):
        try:
            items = self.find_elements(self.locators.CART_ITEMS)
            items_text = [item.text for item in items]
            return items_text
        except Exception:
            return []

    def check_if_item_is_absent_in_shopping_cart(self):

        element = self.find(self.locators.CART_SAUCE_LABS_BACKPACK)
        return len(element) == 0

