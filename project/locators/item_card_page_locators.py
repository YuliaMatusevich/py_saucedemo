from selenium.webdriver.common.by import By


class ItemCardPageLocators:
    ITEM_NAME = By.XPATH, "//div[@class = 'inventory_details_name large_size']"
    ADD_BUTTON_ITEM_CARD = By.XPATH, "//button[text() = 'Add to cart']"
    CART_ICON = By.CLASS_NAME, "shopping_cart_link"
