import allure


@allure.title('Добавление книги в избранное через API')
@allure.feature('API Operations')
@allure.story('Пользователь добавляет книгу в избранное.')
@allure.label('API')
@allure.tag('smoke', 'API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_add_book_to_favorites(api_request):
    url = "/wishlist/arts/65822193"

    response = api_request(url, method='PUT')

    assert response.status_code == 204
    assert response.text == ""