import pytest
from pages.config import ValidDataConfig
from pages.main_page import MainPage
from pages.reg_page import RegPage


@pytest.mark.regression
def test_page_register(browser):
    """Регистрация нового пользователя,
    без подтверждения"""
    page = RegPage(browser, ValidDataConfig.REG_PAGE_LINK)
    page.open()
    page.go_to_reg_login()
    page.go_to_reg_password()
    page.go_to_reg_password_cfm()
    # page.submit_to_reg_btn()


@pytest.mark.xfail(reason='Негативный тест, неверно указано подтверждение пароля.')
def test_go_main_page_to_register_page(browser):
    """Пользователь заходит на главную страницу,
    нажимает кнопку регистрации и вводит свои данные,
    ошибается в поле подтверждения пароля.
    Ожидание регистрация не происходит!"""
    page = MainPage(browser, ValidDataConfig.MAIN_PAGE_LINK)
    page.open()
    page.go_to_register_page()
    page = RegPage(browser, ValidDataConfig.REG_PAGE_LINK)
    page.open()
    page.go_to_reg_login()
    page.go_to_reg_password()
    page.go_to_reg_password_cfm()
    page.submit_to_reg_btn()
    current_url = browser.current_url  # Текущий URL
    assert ValidDataConfig.PROFILE_PAGE != current_url, 'Пользователю не удалось зарегистрироваться'
