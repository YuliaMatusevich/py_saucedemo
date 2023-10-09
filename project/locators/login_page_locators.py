from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME_FIELD = By.ID, "user-name"
    PASSWORD_NAME_FIELD = By.ID, "password"
    LOGIN_BUTTON = By.ID, "login-button"
    ERROR_MESSAGE = By.XPATH, "//h3"
