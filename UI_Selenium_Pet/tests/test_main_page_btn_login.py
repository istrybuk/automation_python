import pytest
import time
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


@pytest.mark.main
def test_registration_button_on_page(browser):
    """Кнопка регистрации на главной странице"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_register_page()


def test_dropdown_on_page(browser):
    """Выпадающий список на главной странице"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.select_dropdown()


def test_filter_on_page(browser):
    """Фильтр на главной странице"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.filter_usage()


def test_end_and_beginning_page(browser):
    """Кнопки страниц начала и конец"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_paginator_end_pages()
    page.go_to_paginator_beginning_pages()


def test_paginator_full_check(browser):
    """Следящая страница, в конец, прошлая страница, в начало"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_paginator_next_pages()
    page.go_to_paginator_end_pages()
    page.go_to_paginator_previous_pages()
    page.go_to_paginator_beginning_pages()


def test_next_and_previous_page(browser):
    """Кнопки страниц следующая и предыдущая"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_paginator_next_pages()
    page.go_to_paginator_previous_pages()


def test_paginator_click_pages(browser):
    """Выбор рандомной страны"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.paginator_random_click_pages()
    time.sleep(4)
