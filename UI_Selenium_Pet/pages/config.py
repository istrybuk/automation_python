"""Данные"""


class ValidDataConfig:
    VAL_LOGIN = 'Sivan@bk.by'
    VAL_PASS = '123Qaz'
    MAIN_PAGE_LINK = 'http://34.141.58.52:8080/#/'
    LOGIN_PAGE_LINK = 'http://34.141.58.52:8080/#/login'
    REG_PAGE_LINK = 'http://34.141.58.52:8080/#/register'
    PROFILE_PAGE = 'http://34.141.58.52:8080/#/profile'


class InvalidDataConfig:
    INVAL_LOGIN = 'test1@bk.ru'
    INVAL_PASS = '12345'
    INVAL_PASS_CFM = '1234'  # Подтверждение правильности ввода пароля
    # MAIN_LINK = ''
    LOGIN_LINK = 'http://34.141.58.52:8080/#/logins'
