import time

from project.pages.base_page import BasePage
from project.locators.login_page_locators import LoginPageLocators
from project.pages.catalog_page import CatalogPage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def login_standard(self):
        self.find(self.locators.USER_NAME_FIELD).send_keys("standard_user")
        self.find(self.locators.PASSWORD_NAME_FIELD).send_keys("secret_sauce")
        self.find(self.locators.LOGIN_BUTTON).click()
        return CatalogPage(driver=self.driver)

    def login_incorrect(self):
        self.find(self.locators.USER_NAME_FIELD).send_keys("user")
        self.find(self.locators.PASSWORD_NAME_FIELD).send_keys("user")
        self.find(self.locators.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        return self.find(self.locators.ERROR_MESSAGE).text






# def test_auth_locked_out_user(driver):
#     driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     error_message = driver.find_element(By.XPATH, "//h3").text
#     assert (error_message == "Epic sadface: Sorry, this user has been locked out.")
#
#
# def test_auth_problem_user(driver):
#     driver.find_element(By.ID, "user-name").send_keys("problem_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     assert (driver.current_url == "https://www.saucedemo.com/inventory.html")
#
#
# def test_auth_performance_glitch_user(driver):
#     driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     assert (driver.current_url == "https://www.saucedemo.com/inventory.html")
#