from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('Sivan@bk.by')

    def go_to_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('123Qaz')

    def click_to_btn(self):
        click_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        click_btn.submit()
