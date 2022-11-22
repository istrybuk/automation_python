import pytest
from pages.config import *
from pages.main_page import MainPage


@pytest.mark.parametrize('link', [ValidDataConfig.LOGIN_PAGE_LINK,
                                  InvalidDataConfig.LOGIN_LINK])
def test_go_to_login_page(browser, link):
    """Передача двух параметров в link"""
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
