import allure


@allure.title('Удаление книги из корзины через API')
@allure.feature('API Operations')
@allure.story('Удаление книги из корзины.')
@allure.label('API')
@allure.tag('smoke','API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_delete_book_from_favorite(api_request):
    url = "/wishlist/arts/70330762"
    headers = {
        'wishlist': '70330762'
    }
    response = api_request(url, method='DELETE', headers=headers)

    assert response.status_code == 204
    assert response.text == ''