from selenium.webdriver.common.by import By

from conftest import driver
from project.pages.login_page import LoginPage
from project.pages.catalog_page import CatalogPage


def test_login_form(driver):
    assert (driver.current_url, "https://www.saucedemo.com")


def test_auth_standard_user(driver):
    login_page = LoginPage(driver).login_standard()
    assert (login_page.get_url(driver) == "https://www.saucedemo.com/inventory.html")


def test_auth_standard_user_incorrect_credentials(driver):
    error_message = LoginPage(driver).login_incorrect().get_error_message()
    assert (error_message == "Epic sadface: Username and password do not match any user in this service")


def test_add_item_from_catalog(driver):
    item_name = "Sauce Labs Backpack"
    cart_items_names_list = (LoginPage(driver)
                             .login_standard()
                             .add_sauce_labs_backpack()
                             .click_cart_icon()
                             .get_cart_list_items())

    assert (item_name in cart_items_names_list)


def test_delete_item_from_catalog(driver):
    item_name = "Sauce Labs Backpack"
    cart_items_names_list = (LoginPage(driver)
                             .login_standard()
                             .add_sauce_labs_backpack()
                             .click_cart_icon()
                             .get_cart_list_items())

    assert (item_name in cart_items_names_list)

    driver.back()
    catalog_page = CatalogPage(driver).delete_sauce_labs_backpack()

    button_text = catalog_page.get_button_text_sauce_labs_backpack()
    assert (button_text == "Add to cart")

    cart_items_names_list = catalog_page.click_cart_icon().get_cart_list_items()
    assert (item_name not in cart_items_names_list)


# def test_delete_item_from_catalog_BASE (driver, login_standard_user):
#     item_name = "Sauce Labs Backpack"
#     add_item_from_catalog(driver, item_name)
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     items = driver.find_elements(By.CSS_SELECTOR, ".cart_list a>div")
#
#     assert (item_name in [item.text for item in items])
#     driver.back()
#
#     driver.find_element(By.XPATH,
#                         f"//img[@alt = '{item_name}']/../parent::div/following-sibling::div//button[text()='Remove']").click()
#     button_text = driver.find_element(By.XPATH,
#                                       f"//img[@alt = '{item_name}']/../parent::div/following-sibling::div//button").text
#     assert (button_text == "Add to cart")
#     assert (check_if_item_is_absent_in_shopping_cart(driver, item_name))
#
#
def test_add_item_from_card(driver):
    catalog_item_name = "Sauce Labs Backpack"
    card_page = (LoginPage(driver)
                 .login_standard()
                 .click_sauce_labs_backpack_item_name())
    assert card_page.get_item_name() == catalog_item_name

    card_list_items_names = (card_page.click_add_to_cart()
                             .click_cart_icon()
                             .get_cart_list_items())

    assert (catalog_item_name in card_list_items_names)


# def test_add_item_from_card_BASE(driver, login_standard_user):
#     catalog_item_name = "Sauce Labs Backpack"
#     driver.find_element(By.XPATH,
#                         f"//img[@alt = '{catalog_item_name}']/../parent::div/following-sibling::div//a/div").click()
#     card_item_name = driver.find_element(By.XPATH, "//div[@class = 'inventory_details_name large_size']").text
#     assert card_item_name == catalog_item_name
#
#     driver.find_element(By.XPATH, "//button[text() = "Add to cart").click()
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     items = driver.find_elements(By.CSS_SELECTOR, ".cart_list a>div")
#     assert (catalog_item_name in [item.text for item in items])
#
#
# def test_delete_item_from_card(driver, login_standard_user):
#     catalog_item_name = "Sauce Labs Backpack"
#     driver.find_element(By.XPATH,
#                         f"//img[@alt = '{catalog_item_name}']/../parent::div/following-sibling::div//a/div").click()
#     card_item_name = driver.find_element(By.XPATH, "//div[@class = 'inventory_details_name large_size']").text
#     assert card_item_name == catalog_item_name
#
#     driver.find_element(By.XPATH, "//button[text() = 'Add to cart']").click()
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     items = driver.find_elements(By.CSS_SELECTOR, ".cart_list a>div")
#     assert (catalog_item_name in [item.text for item in items])
#
#     driver.back()
#     driver.find_element(By.XPATH, "//button[text() = 'Remove']").click()
#     assert (check_if_item_is_absent_in_shopping_cart(driver, card_item_name))
#
#
# def test_delete_item_from_cart(driver, login_standard_user):
#     item_name = "Sauce Labs Backpack"
#     driver.find_element(By.XPATH,
#                         f"//img[@alt = '{item_name}']/../parent::div/following-sibling::div//button[text()='Add to cart']").click()
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     items = driver.find_elements(By.CSS_SELECTOR, ".cart_list a>div")
#     assert (item_name in [item.text for item in items])
#
#     driver.find_element(By.XPATH,
#                         f"//div[text()='{item_name}']//../following-sibling::div[@class = 'item_pricebar']/button[text() = 'Remove']").click()
#     element = driver.find_elements(By.XPATH, f"//div[text() = '{item_name}']")
#     assert len(element) == 0
#
#
# def test_forward_to_item_card_click_item_name(driver, login_standard_user):
#     item_name = "Sauce Labs Backpack"
#     driver.find_element(By.XPATH, f"//div[text() = '{item_name}']").click()
#     card_item_name = driver.find_element(By.XPATH,
#                                          "//div[@class= 'inventory_details'] //div[@class='inventory_details_name large_size']").text
#
#     assert (card_item_name == item_name)
#
#
# def test_forward_to_item_card_click_item_image(driver, login_standard_user):
#     item_name = "Sauce Labs Backpack"
#     driver.find_element(By.CSS_SELECTOR, f"img[alt  = '{item_name}']").click()
#     card_item_name = driver.find_element(By.XPATH,
#                                          "//div[@class= 'inventory_details'] //div[@class='inventory_details_name large_size']").text
#
#     assert (card_item_name == item_name)
#
#
# def test_sort_A_to_Z(driver, login_standard_user):
#     expected_list = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
#                      'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
#     expected_list1 = []
#     for i in elements:
#         expected_list1.append(i.text)
#     expected_list1.sort()
#
#     select = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
#     select.select_by_value("az")
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
#     actual_list = []
#     for i in elements:
#         actual_list.append(i.text)
#
#     # print(expected_list)
#     # print(expected_list1)
#     # print(actual_list)
#     assert expected_list == actual_list
#     assert expected_list1 == actual_list
#     assert expected_list == actual_list
#
#
# def test_sort_Z_to_A(driver, login_standard_user):
#     expected_list = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
#                      'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
#     expected_list1 = []
#     for i in elements:
#         expected_list1.append(i.text)
#     expected_list1.sort(reverse=True)
#
#     select = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
#     select.select_by_value("za")
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
#     actual_list = []
#     for i in elements:
#         actual_list.append(i.text)
#
#     # print(expected_list)
#     # print(expected_list1)
#     # print(actual_list)
#     assert expected_list == actual_list
#     assert expected_list1 == actual_list
#     assert expected_list == actual_list
#
#
# def test_sort_low_to_high(driver, login_standard_user):
#     expected_list = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
#     expected_list1 = []
#     for i in elements:
#         expected_list1.append(float(i.text[1:]))
#     expected_list1.sort()
#
#     select = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
#     select.select_by_value("lohi")
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
#     actual_list = []
#     for i in elements:
#         actual_list.append(float(i.text[1:]))
#
#     # print(expected_list)
#     # print(expected_list1)
#     # print(actual_list)
#     assert expected_list == actual_list
#     assert expected_list1 == actual_list
#     assert expected_list == actual_list
#
#
# def test_sort_high_to_low(driver, login_standard_user):
#     expected_list = [49.99, 29.99, 15.99, 15.99, 9.99, 7.99]
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
#     expected_list1 = []
#     for i in elements:
#         expected_list1.append(float(i.text[1:]))
#     expected_list1.sort(reverse=True)
#
#     select = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
#     select.select_by_value("hilo")
#     elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
#     actual_list = []
#     for i in elements:
#         actual_list.append(float(i.text[1:]))
#
#     # print(expected_list)
#     print(expected_list1)
#     print(actual_list)
#     assert expected_list == actual_list
#     assert expected_list1 == actual_list
#     assert expected_list == actual_list
#
#
# def test_logout(driver, login_standard_user):
#     # driver.find_element(By.CSS_SELECTOR, ".bm-burger-button").click()
#     action = ActionChains(driver)
#     action.click(driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")).perform()
#     time.sleep(0.1)
#     driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link").click()
#     assert (driver.current_url, BASE_URL)
#
#
# def test_about(driver, login_standard_user):
#     action = ActionChains(driver)
#     action.click(driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")).perform()
#     time.sleep(0.1)
#     driver.find_element(By.CSS_SELECTOR, "#about_sidebar_link").click()
#     assert (driver.current_url, "https://saucelabs.com/")
#
#
# def test_reset_app(driver, login_standard_user):
#     item_name_1 = "Sauce Labs Backpack"
#     item_name_2 = "Test.allTheThings() T-Shirt (Red)"
#     item_name_3 = "Sauce Labs Bike Light"
#     add_item_from_catalog(driver, item_name_1)
#     add_item_from_catalog(driver, item_name_2)
#     add_item_from_catalog(driver, item_name_3)
#
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     element = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
#     assert len(element) == 3
#
#     action = ActionChains(driver)
#     action.click(driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")).perform()
#     time.sleep(0.1)
#     driver.find_element(By.CSS_SELECTOR, "#reset_sidebar_link").click()
#     assert (driver.current_url, "https://saucelabs.com/")
#
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     element = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
#     assert len(element) == 0
#
#
# def test_end_to_end_order_from_catalog(driver, login_standard_user):
#     item_name = "Sauce Labs Backpack"
#     item_price = 29.99
#     item_tax = 2.40
#
#     catalog_price = float(
#         driver.find_element(By.XPATH, f"//div[text() = '{item_name}']/../../following-sibling::div/div").text[1:])
#     add_item_from_catalog(driver, item_name)
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.ID, "checkout").click()
#     driver.find_element(By.ID, "first-name").send_keys("Jim")
#     driver.find_element(By.ID, "last-name").send_keys("Beam")
#     driver.find_element(By.ID, "postal-code").send_keys("123456")
#     driver.find_element(By.ID, "continue").click()
#
#     cart_tax = float(driver.find_element(By.CSS_SELECTOR, ".summary_tax_label").text[6:])
#     cart_total = float(
#         driver.find_element(By.XPATH, "//div[@class = 'summary_info_label summary_total_label']").text[8:])
#     print(cart_total)
#
#     cart_price = float(driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text[1:])
#     assert (driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == item_name)
#     assert (cart_price == item_price)
#     assert (cart_price == catalog_price)
#     assert (driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1")
#     assert (driver.find_element(By.XPATH, "//div[text() ='SauceCard #31337']").is_displayed())
#     assert (driver.find_element(By.XPATH, "//div[text() ='Free Pony Express Delivery!']").is_displayed())
#     assert (driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label").text[13:] == str(catalog_price))
#     assert (cart_tax == item_tax)
#     assert (cart_total == item_price + item_tax)
#
#     driver.find_element(By.ID, "finish").click()
#
#     assert (driver.current_url, "https://www.saucedemo.com/checkout-complete.html")
#     assert (driver.find_element(By.CSS_SELECTOR, ".title").text == "Checkout: Complete!")
#     assert (driver.find_element(By.CSS_SELECTOR, "img[alt = 'Pony Express']").is_displayed())
#     assert (driver.find_element(By.XPATH, "//h2").text == "Thank you for your order!")
#     assert (driver.find_element(By.CLASS_NAME, "complete-text").text ==
#             "Your order has been dispatched, and will arrive just as fast as the pony can get there!")
#     assert (driver.find_element(By.ID, "back-to-products").is_displayed())
