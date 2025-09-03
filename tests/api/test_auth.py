import os
import allure
from dotenv import load_dotenv



@allure.title('Успешная авторизация через API litres.ru')
@allure.feature('Email Auth')
@allure.story('Пользователь успешно авторизуется по email')
@allure.label('API')
@allure.tag('smoke', 'API')
@allure.severity('critical')
@allure.label("owner", "D. Efimov")
def test_auth(api_request):
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')
    url = "/auth/login"

    data = {
        "login": login,
        "password": password
    }

    headers = {
        'ab-tests-flags': '[{"v":"false","t":"flag","n":"ppd444"},{"v":"false","t":"flag","n":"acqn1862_rk_back"}]',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,az;q=0.7',
        'app-id': '115',
        'baggage': 'sentry-environment=prod,sentry-release=6.845.83,sentry-public_key=66365c10274f4724819f92df56571b8b,sentry-trace_id=de0b209257dd4dcca69164cd18ce7fa7,sentry-sample_rate=0.4,sentry-transaction=%2F,sentry-sampled=false',
        'cache-control': 'no-cache',
        'client-host': 'www.litres.ru',
        'content-type': 'application/json',
        'origin': 'https://www.litres.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.litres.ru/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sentry-trace': 'de0b209257dd4dcca69164cd18ce7fa7-831874f4571f6999-0',
        'session-id': '6ofe88b4b524895i7v1l7gfna2893w7n',
        'ui-currency': 'RUB',
        'ui-language-code': 'ru',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'x-request-id': 'aa66852edcc5c5412667918d9ff87470',
    }

    cookies = {
        '_ym_uid': '1752170955462978022',
        '_ym_d': '1752170955',
        'uxs_uid': 'fd87b3a0-5db8-11f0-bbb3-1fb66c660dfd',
        'mindboxDeviceUUID': '3a33539a-6a74-40e1-ad99-dd93062c84fc',
        'directCrm-session': '{"deviceGuid":"3a33539a-6a74-40e1-ad99-dd93062c84fc"}',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998=1|||1471519752600=1|||1471519752605=1',
        '__ddg1_': 'qsZ9CStVCT7PgobtW32N',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        '__Secure-session_context': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI2ZjN4ODA2d2I4Y3g4NDJhN28xZzEyZGZiNzk5Mm04MSIsInVzZXJfaWQiOjEyNjg2MTU0NjgsImF1dGhfbWV0aG9kIjoibG9naW5fb3JfZW1haWwiLCJpc3N1ZWRfYXQiOjE3NTY5MTgyMTB9.qgbiVA6J5PUzPGvlGRZNF9FT18RjrnmcuOewK5xAI00',
        '__ddg9_': '95.107.69.25',
        '__ddg10_': '1756919718',
        '__ddg8_': 'jtSeH2V6xRkh1xvU'
    }

    response = api_request(url, method='POST', data=data, headers=headers, cookies=cookies)

    assert response.status_code == 200
    body = response.json()
    assert body.get("error") is None