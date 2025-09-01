import os
import allure
from dotenv import load_dotenv
from litres_test.schema import schemas
from jsonschema import validate


@allure.title('Successful user auth with email')
@allure.feature('Email Auth')
@allure.story('User, to successfully authenticated using email credentials.')
@allure.label('API')
@allure.tag('smoke', 'API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_auth(api_request):
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')
    BASE_URL = os.getenv('BASE_URL')

    url = "/auth/login"
    data = {"login": login, "password": password}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Origin": "https://www.litres.ru",
        "Referer": "https://www.litres.ru/",
        "X-Requested-With": "XMLHttpRequest"
    }
    response = api_request(url, method='POST', data=data, headers=headers)
    body = response.json()

    print(f"Requesting: {BASE_URL + url}")
    print(f"Login: {login}, Password: {password}")
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")

    assert response.status_code == 200
    validate(body, schema=schemas.post_authorization_schema)
    assert body['error'] is None