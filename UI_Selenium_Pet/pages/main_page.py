from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        self.browser.find_element(*MainPageLocators.REGISTER_LINK).click()

    def select_dropdown(self):
        self.browser.find_element(*MainPageLocators.DROPDOWN_LINK).click()
        self.browser.find_element(*MainPageLocators.DROPDOWN_VALUE).click()

    """ чем можно заменить + Keys.ENTER ?"""

    def filter_usage(self):
        self.browser.find_element(*MainPageLocators.FILTER_LINK).send_keys('Duff' + Keys.ENTER)

    def paginator(self):
        pass
