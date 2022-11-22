from pages.main_page import MainPage


def test_dropdown_on_page(browser):
    """Выпадающий список на главной странице"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_dropdown()
