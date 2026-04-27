import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_resta(client):
    rv = client.get('/resta?a=20&b=8')
    assert rv.status_code == 200
    assert rv.get_json()['resultado'] == 12
