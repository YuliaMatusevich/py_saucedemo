from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def get_url(self, driver):
        return driver.current_url

    def find(self, locator, timeout=1):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=1):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def back(self):
        return self.driver.back()

# def open(self):
#     self.driver.get(self.url)
#
# def element_is_visible(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
#
# def elements_are_visible(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
#
# def element_is_present(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
#
# def elements_are_present(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
#
# def element_is_not_visible(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
#
# def element_is_clickable(self, locator, timeout=5):
#     return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
#
# def scroll_to_element(self, element):
#     self.driver.execute_script("argument[0].scrollIntoView();", element)
