from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LOGIN = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BTN = (By.CLASS_NAME, 'p-button-label')


class RegisterPageLocators:
    REG_LOGIN = (By.ID, 'login')
    REG_PASS = (By.CSS_SELECTOR, '#password > input')
    REG_PASS_CFM = (By.CSS_SELECTOR, '#confirm_password > input')
    REG_BTN = (By.CLASS_NAME, 'p-button p-component')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app>header>div>ul>li>a')
    REGISTER_LINK = (By.CSS_SELECTOR, '#app>header>div>ul>li:nth-of-type(2)')
    DROPDOWN_LINK = (By.CLASS_NAME, 'p-dropdown-trigger')
    DROPDOWN_VALUE = (By.ID, 'pv_id_2_2')
    FILTER_LINK = (By.ID, 'petName')
    PAGINATOR_NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div/div/button[3]')
    PAGINATOR_PREVIOUS_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div/div/button[2]')
    PAGINATOR_BEGINNING_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div/div/button[1]')
    PAGINATOR_END_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div/div/button[4]')
    PAGINATOR_PAGES = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/span/button')
