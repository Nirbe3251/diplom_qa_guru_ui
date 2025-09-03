import allure

from litres_test.schema import schemas
from jsonschema import validate


@allure.title('Успешный поиск книги по названию и типу')
@allure.feature('Поиск книги')
@allure.story('Поиск книги по названию и типу')
@allure.label('API')
@allure.tag('smoke', 'API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_get_search_book(api_request):
    book_title = 'Франк Тилье Головоломка'
    art_types = 'text_book'
    types = 'text_book'
    url = f"/search?q={book_title}&art_types={art_types}&types={types}"
    response = api_request(url)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.get_search_book)
    assert body['payload']['data'][0]['instance']['title'] == 'Головоломка'
    assert body['payload']['data'][0]['type'] == 'text_book'
    assert body['payload']['data'][0]['instance']['persons'][0]['full_name'] == 'Франк Тилье'