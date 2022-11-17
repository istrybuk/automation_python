import time
from pages.main_page import MainPage


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_usage()

    time.sleep(5)
