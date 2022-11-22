from .base_page import BasePage
from .config import InvalidDataConfig
from .locators import RegisterPageLocators


class RegPage(BasePage):
    def go_to_reg_login(self):
        self.browser.find_element(*RegisterPageLocators.REG_LOGIN).send_keys(InvalidDataConfig.INVAL_LOGIN)

    def go_to_reg_password(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS).send_keys(InvalidDataConfig.INVAL_PASS)

    def go_to_reg_password_cfm(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS_CFM).send_keys(InvalidDataConfig.INVAL_PASS_CFM)

    def submit_to_reg_btn(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS).submit()
