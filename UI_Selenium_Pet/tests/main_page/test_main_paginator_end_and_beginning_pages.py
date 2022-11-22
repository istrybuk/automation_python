from pages.main_page import MainPage


def test_end_and_beginning_page(browser):
    """Кнопки страниц начала и конец"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_paginator_end_pages()
    page.go_to_paginator_beginning_pages()
