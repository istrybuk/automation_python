import time
from pages.main_page import MainPage


def test_paginator_click_pages(browser):
    """Выбор рандомной страны"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.paginator_random_click_pages()
    time.sleep(4)
