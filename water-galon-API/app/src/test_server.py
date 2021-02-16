from fastapi.testclient import TestClient

from src.server import api

client = TestClient(api)


def test_root():
    response = client.get("/")
    assert response.status_code == 200