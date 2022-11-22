from pages.main_page import MainPage


def test_filter_on_page(browser):
    """Фильтр на главной странице"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_usage()
