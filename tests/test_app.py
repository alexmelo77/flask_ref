import pytest
from ast import literal_eval

from fet.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_get(client):
    response = client.get('http://localhost:5000/hello_get?myint=1')
    print(response)
    assert response.status_code == 200
    d = literal_eval(response.data.decode('utf8'))
    assert d == {'myint': 1}


def test_hello_post(client):
    payload = {'code': 7}
    response = client.post(
        'http://localhost:5000/hello_post', data=payload)
    assert response.status_code == 200
    d = literal_eval(response.data.decode('utf8'))
    assert d == {"code squared": 49}


