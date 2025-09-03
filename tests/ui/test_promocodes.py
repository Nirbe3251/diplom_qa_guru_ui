import allure

from litres_test.pages.promocode_page import PromocodePage\

@allure.title('Активация промокода litres.ru')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_activate_promocode():
    promocode_page = PromocodePage()

    with allure.step("Открываем браузер"):
        promocode_page.browser_open()

    with allure.step("Переходим на страницу промокодов"):
        promocode_page.redirect_to_promocodes()

    with allure.step('Заполняем поле промокода'):
        promocode_page.fill_promocode_input('promokodibonus2')

    with allure.step("Нажимаем кнопку Активировать"):
        promocode_page.click_activation_button()

# @allure.title('Негативная активация промокода с пустым полем litres.ru')
# @allure.label('UI')
# @allure.tag('smoke')
# @allure.severity('critical')
# @allure.label("owner", "D. Efimov")
# def test_fiil_empty_promocode():
#     promocode_page = PromocodePage()
#
#     with allure.step("Открываем браузер"):
#         promocode_page.browser_open()
#
#     with allure.step("Переходим на страницу промокодов"):
#         promocode_page.redirect_to_promocodes()
#
#     with allure.step('Заполняем поле промокода'):
#         promocode_page.fill_empty_value_in_promo_input(' ')
#
#     with allure.step("Нажимаем кнопку Активировать"):
#         promocode_page.click_activation_button()
#
#     with allure.step('Проверяем ошибку пустого промокода'):
#         promocode_page.error_with_empty_promo_input()
#
# @allure.title('Негативная активация промокода с невалидным(несуществующим) промокодом litres.ru')
# @allure.label('UI')
# @allure.tag('smoke')
# @allure.severity('critical')
# @allure.label("owner", "D. Efimov")
# def test_invalid_promocode():
#     promocode_page = PromocodePage()
#
#     with allure.step("Открываем браузер"):
#         promocode_page.browser_open()
#
#     with allure.step("Переходим на страницу промокодов"):
#         promocode_page.redirect_to_promocodes()
#
#     with allure.step('Заполняем поле промокода'):
#         promocode_page.fill_empty_value_in_promo_input(' ')
#
#     with allure.step("Нажимаем кнопку Активировать"):
#         promocode_page.click_activation_button()
#
#     with allure.step('Проверяем ошибку неправильного промокода'):
#         promocode_page.error_with_empty_promo_input()


