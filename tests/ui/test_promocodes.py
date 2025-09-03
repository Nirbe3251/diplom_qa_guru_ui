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
        promocode_page.fill_promocode_input('promokodi30j')

    with allure.step("Нажимаем кнопку Активировать"):
        promocode_page.click_activation_button()

    with allure.step("Проверяем, что промокод активирован"):
        promocode_page.check_activate_promocode()


