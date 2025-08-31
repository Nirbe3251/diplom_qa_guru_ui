import allure

from litres_test.pages.main_page import MainPage

def test_add_book_in_the_cart():
    main_page = MainPage()
    with allure.step("Открыть litres"):
        main_page.browser_open()

    with allure.step("Поиск книги"):
        main_page.search_book("стивен кинг мёртвая зона")

    with allure.step("Открыть книгу"):
        main_page.open_book()

    with allure.step("Добавить книгу в корзину"):
        main_page.add_book_in_the_cart()




