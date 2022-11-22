import pytest
from pages.main_page import MainPage
from pages.config import *


@pytest.mark.main
def test_login_button_on_page(browser):
    """Кнопка логин на главной странице,
    проверка перехода на правильный URL"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    current_url = browser.current_url
    assert current_url == ValidDataConfig.LOGIN_PAGE_LINK
