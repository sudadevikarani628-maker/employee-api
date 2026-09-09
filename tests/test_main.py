from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee API is running"
    }


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) == 3