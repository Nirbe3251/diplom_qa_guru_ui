from selene import browser, have, be


class MainPage:
    def browser_open(self):
        browser.open("https://www.litres.ru/")

    def search_book(self, value):
        browser.element("[name='q']").type(value).press_enter()

    def open_book(self):
        browser.element('[data-testid="art__title"][href="/audiobook/stiven-king/mertvaya-zona-65822193/"]').should(be.visible).click()
        browser.driver.switch_to.window(browser.driver.window_handles[-1])

    def switch_text_version_book(self):
        browser.element('[data-testid="book-tabs-format__element_текст"]').click()

    def open_text_preview(self):
        browser.element('[data-testid="book__fragmentReadListen--button"]').click()

    def add_book_in_the_cart(self):
        element = browser.element("[data-testid='book__addToCartButton']").should(be.visible)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element.locate())
        element.should(be.clickable).click()

    def redirect_to_cart(self):
        browser.element('[data-testid="modal__close--button"]').click()
        browser.element("[data-testid='book__goToCartButton']").click()

    def remove_book_from_the_cart(self):
        browser.element("[data-testid='cart__listDeleteButton']").click()
        browser.element('//*[@id="modal"]/div[3]/div/div/div/div/div[3]/button[1]').click()

    def cart_is_not_empty(self):
        return browser.element("[data-testid='cart__listDeleteButton']").matching(be.visible)

    def open_page_my_books(self):
        browser.element('[data-testid="tab-myBooks"]').click()

    def choise_book(self):
        browser.element('[data-testid="button__content"]').click()

