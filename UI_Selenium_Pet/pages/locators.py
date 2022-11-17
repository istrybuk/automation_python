from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BTN = (By.CLASS_NAME, 'p-button-label')


class RegisterPageLocators:
    LOGIN_EMAIL = ()
    LOGIN_PASS = ()
    LOGIN_BTN = ()


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app>header>div>ul>li>a')
    REGISTER_LINK = (By.CSS_SELECTOR, '#app>header>div>ul>li:nth-of-type(2)')
    DROPDOWN_LINK = (By.CLASS_NAME, 'p-dropdown-trigger')
    DROPDOWN_VALUE = (By.ID, 'pv_id_2_2')
    FILTER_LINK = (By.ID, 'petName')
    PAGINATOR = ()
