from pages.main_page import MainPage


def test_next_and_previous_page(browser):
    """Кнопки страниц следующая и предыдущая"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_paginator_next_pages()
    page.go_to_paginator_previous_pages()
