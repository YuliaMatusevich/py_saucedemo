from selenium.webdriver.common.by import By


class CartPageLocators:
    CART_ITEMS = By.CSS_SELECTOR, ".cart_list a>div"
    CART_SAUCE_LABS_BACKPACK = By.XPATH, "//div[text() = '{item_name}']"

