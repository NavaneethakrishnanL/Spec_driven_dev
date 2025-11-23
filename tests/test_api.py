from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_user_ok():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
