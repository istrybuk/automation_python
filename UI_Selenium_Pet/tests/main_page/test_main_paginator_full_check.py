from pages.main_page import MainPage


def test_paginator_full_check(browser):
    """Следящая страница, в конец, прошлая страница, в начало"""
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_paginator_next_pages()
    page.go_to_paginator_end_pages()
    page.go_to_paginator_previous_pages()
    page.go_to_paginator_beginning_pages()
