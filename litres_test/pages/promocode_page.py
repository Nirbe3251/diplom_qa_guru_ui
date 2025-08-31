from selene import browser, have, be

class PromocodePage:
    def browser_open(self):
        browser.open("https://www.litres.ru/")

    def redirect_to_promocodes(self):
        browser.element('[data-testid="lowerMenu__item--promoCodes"]').click()

    def fill_promocode_input(self, value):
        browser.element('[name="promocode"]').type(value)

    def click_activation_button(self):
        browser.element('[data-testid="button__content"]').click()

    def fill_empty_value_in_promo_input(self, value):
        browser.element('[name="promocode"]').type(value)

    def error_with_empty_promo_input(self):
        browser.element('[data-testid="textbox--input__error"]').should(be.visible).should(have.exact_text('Неверный формат промокода. Попробуйте еще раз')
        )

    def fill_negative_value_in_promo_input(self, value):
        browser.element('[name="promocode"]').type(value)
