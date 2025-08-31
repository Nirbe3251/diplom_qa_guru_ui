from selene import browser, have, be

class LoginPage:
    def browser_open(self):
        browser.open("https://www.litres.ru/")

    def open_login_popup(self):
        browser.element('[data-testid="user-button"]').should(be.clickable).click()

    def fill_email(self, value):
        browser.element('[name="email"]').type(value)
        browser.element('[data-testid="auth__button--continue"]').click()

    def fill_password(self, value):
        browser.element('[name="pwd"]').type(value)
        browser.element('[data-testid="auth__button--enter"]').click()

    def error_with_empty_email(self):
        browser.element('[data-testid="textbox--input__error"]').should(have.text('Поле не может быть пустым'))

    def error_with_empty_pass(self):
        browser.element('[data-testid="textbox--input__error"]').should(have.text('Введите пароль'))