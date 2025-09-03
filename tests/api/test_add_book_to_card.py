import allure
from litres_test.schema import schemas
from jsonschema import validate

@allure.title('Добавление книги неавторизованным пользователем')
@allure.feature('Пользователь неавторизован')
@allure.label('API')
@allure.tag('smoke','API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_add_book_to_cart(api_request):
    art_ids = [65822193]
    url = "/cart/arts/add"
    data = {"art_ids": art_ids}
    response = api_request(url, method='PUT', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.put_add_books_to_cart)
    assert body['payload']['data']['added_art_ids'] == art_ids
    assert body['payload']['data']['failed_art_ids'] == []