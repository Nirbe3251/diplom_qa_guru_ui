import allure

from litres_test.pages.login_page import LoginPage

def test_login():
    login_page = LoginPage()

    with allure.step("Открываем браузер"):
        login_page.browser_open()

    with allure.step("Открываем попап логина"):
        login_page.open_login_popup()

    with allure.step("Заполняем почту"):
        login_page.fill_email('daniil.efimow@mail.ru')

    with allure.step("Заполняем пароль"):
        login_page.fill_password('dandris2003')

def test_login_without_email():
    login_page = LoginPage()

    with allure.step("Открываем браузер"):
        login_page.browser_open()

    with allure.step("Открываем попап логина"):
        login_page.open_login_popup()

    with allure.step("Заполняем почту пустым названием"):
        login_page.fill_email('')

    with allure.step('Проверяем ошибку на пустую почту'):
        login_page.error_with_empty_email()

def test_login_without_pass():
    login_page = LoginPage()

    with allure.step("Открываем браузер"):
        login_page.browser_open()

    with allure.step("Открываем попап логина"):
        login_page.open_login_popup()

    with allure.step("Заполняем почту"):
        login_page.fill_email('daniil.efimow@mail.ru')

    with allure.step('Заполняем пустой пароль'):
        login_page.fill_password('')

    with allure.step('Проверяем ошибку пароля'):
        login_page.error_with_empty_pass()