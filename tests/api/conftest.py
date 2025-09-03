import json
import os
import requests
from allure_commons.types import AttachmentType
import logging
import allure
import pytest
from dotenv import load_dotenv


@pytest.fixture
def api_request():
    load_dotenv()
    BASE_URL = os.getenv('BASE_URL')
    def _make_api_request(url, method="GET", data=None, headers=None, cookies=None):
        url = BASE_URL + url
        with allure.step(f"API Request: {method}"):
            if method not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                raise ValueError("Unsupported HTTP method")

            response = None

            try:
                if method == "GET":
                    response = requests.get(url, headers=headers, cookies=cookies)
                elif method == "POST":
                    if headers and headers.get("Content-Type") == "application/x-www-form-urlencoded":
                        response = requests.post(url, data=data, headers=headers, cookies=cookies)
                    else:
                        response = requests.post(url, json=data, headers=headers, cookies=cookies)
                elif method == "PUT":
                    response = requests.put(url, json=data, headers=headers, cookies=cookies)
                elif method == "PATCH":
                    response = requests.patch(url, json=data, headers=headers, cookies=cookies)
                elif method == "DELETE":
                    response = requests.delete(url, headers=headers, cookies=cookies)

                allure.attach(
                    body=response.request.method + " " + response.request.url,
                    name="Request",
                    attachment_type=AttachmentType.TEXT,
                    extension="txt",
                )
                if response.content:
                    allure.attach(
                        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                        name="Response",
                        attachment_type=AttachmentType.JSON,
                        extension="json",
                    )
                logging.info(response.request.url)
                logging.info(response.status_code)
                logging.info(response.text)
                return response
            except Exception as e:
                allure.attach(
                    body=f"Error occurred: {str(e)}",
                    name="Error",
                    attachment_type=AttachmentType.TEXT,
                    extension="txt",
                )
                raise e

    return _make_api_request