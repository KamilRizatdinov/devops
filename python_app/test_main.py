from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_base_route():
    response = client.get("/")
    assert response.status_code == 200


def test_get_unknown_route():
    response = client.get("/unknown")
    assert response.status_code == 404
