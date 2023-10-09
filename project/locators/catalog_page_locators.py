from selenium.webdriver.common.by import By


class CatalogPageLocators:
    item_name = ""
    ADD_BUTTON_SAUCE_LABS_BACKPACK = By.ID, "add-to-cart-sauce-labs-backpack"
    CART_ICON = By.CLASS_NAME, "shopping_cart_link"
    REMOVE_BUTTON_SAUCE_LABS_BACKPACK = By.ID, "remove-sauce-labs-backpack"
    ADD_REMOVE_BUTTON_SAUCE_LABS_BACKPACK = By.XPATH, f"//img[@alt = 'Sauce Labs Backpack']/../parent::div/following-sibling::div//button"
    CATALOG_NAME_SAUCE_LABS_BACKPACK = By.XPATH, f"//img[@alt = 'Sauce Labs Backpack']/../parent::div/following-sibling::div//a/div"