import pytest
import requests
import json


def test_hello_get():
    response = requests.get(
        'http://localhost:5000/hello_get?myint=1')
    assert response.status_code == 200
    d = response.json()
    assert d == {'myint': 1}


def test_hello_post():
    payload = {'code': 7}
    response = requests.post(
        'http://localhost:5000/hello_post', data=payload)
    assert response.status_code == 200
    d = response.json()
    assert d == {"code squared": 49}



