import pytest
from pages.config import *
from pages.main_page import MainPage


@pytest.mark.skip(reason='В настоящее время нет возможности проверить это')
@pytest.mark.parametrize('link', [ValidDataConfig.LOGIN_PAGE_LINK,
                                  InvalidDataConfig.LOGIN_LINK])
def test_go_to_login_page(browser, link):
    """Передача двух параметров в link,
    валидной и не валидной страницы"""
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
