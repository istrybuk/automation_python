import pytest
from pages.reg_page import RegPage


@pytest.mark.regression
def test_page_register(browser):
    """Регистрация нового пользователя"""
    link = 'http://34.141.58.52:8080/#/register'
    page = RegPage(browser, link)
    page.open()
    page.go_login()
    page.go_to_reg_password()
    page.go_to_reg_password_cfm()
    # page.submit_to_reg_btn()
