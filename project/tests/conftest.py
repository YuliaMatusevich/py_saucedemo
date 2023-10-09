import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
