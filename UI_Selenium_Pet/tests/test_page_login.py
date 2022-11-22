import pytest
from pages.config import *
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.regression
def test_page_login(browser):
    """Страница входа пользователя"""
    page = LoginPage(browser, ValidDataConfig.LOGIN_PAGE_LINK)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.click_to_btn()


def test_go_main_page_to_login_page(browser):
    """Пользователь заходит на главную страницу,
    нажимает кнопку логин и вводит свои данные"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, ValidDataConfig.LOGIN_PAGE_LINK)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.click_to_btn()
