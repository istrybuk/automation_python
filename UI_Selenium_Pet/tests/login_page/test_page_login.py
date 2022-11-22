import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_page_login(browser):
    """Страница входа пользователя"""
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.click_to_btn()
