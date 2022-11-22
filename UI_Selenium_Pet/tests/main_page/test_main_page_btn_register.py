import pytest
from pages.main_page import MainPage


@pytest.mark.main
def test_registration_button_on_page(browser):
    """Кнопка регистрации на главной странице"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
