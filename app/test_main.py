import pytest
from app.main import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_add(client):
    res = client.get('/add?a=10&b=5')
    assert res.json['result'] == 15.0


def test_subtract(client):
    res = client.get('/subtract?a=10&b=5')
    assert res.json['result'] == 5.0


def test_multiply(client):
    res = client.get('/multiply?a=4&b=3')
    assert res.json['result'] == 12.0


def test_divide(client):
    res = client.get('/divide?a=10&b=2')
    assert res.json['result'] == 5.0


def test_divide_by_zero(client):
    res = client.get('/divide?a=10&b=0')
    assert res.status_code == 400