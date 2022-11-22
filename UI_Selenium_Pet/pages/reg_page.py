from .base_page import BasePage
from .locators import RegisterPageLocators


class RegPage(BasePage):
    def go_login(self):
        self.browser.find_element(*RegisterPageLocators.REG_LOGIN).send_keys('test1@bk.ru')

    def go_to_reg_password(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS).send_keys('12345')

    def go_to_reg_password_cfm(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS_CFM).send_keys('12345')

    def submit_to_reg_btn(self):
        self.browser.find_element(*RegisterPageLocators.REG_PASS).submit()
