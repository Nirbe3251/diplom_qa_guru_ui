import allure

from litres_test.pages.main_page import MainPage


def test_page_my_book():
    main_page = MainPage()

    with allure.step("Открываем браузер"):
        main_page.browser_open()

    with allure.step("Открываем страницу Мои книги"):
        main_page.open_page_my_books()

    with allure.step("Нажимаем на кнопку Выбрать книги"):
        main_page.choise_book()
