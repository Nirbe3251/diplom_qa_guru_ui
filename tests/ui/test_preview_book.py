import allure

from litres_test.pages.main_page import MainPage


def test_preview_book():
    main_page = MainPage()

    with allure.step("Открываем браузер"):
        main_page.browser_open()

    with allure.step("Ищем книгу"):
        main_page.search_book("стивен кинг мертвая зона")

    with allure.step("Открываем книгу"):
        main_page.open_book()

    with allure.step("Переходим на текствую версию книги"):
        main_page.switch_text_version_book()

    with allure.step("Открываем превью книги"):
        main_page.open_text_preview()

