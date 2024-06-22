import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_addition():
    response = client.post("/add", json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert response.json() == {"result": 10}

def test_addition_empty_list():
    response = client.post("/add", json={"numbers": []})
    assert response.status_code == 422

def test_addition_single_element():
    response = client.post("/add", json={"numbers": [42]})
    assert response.status_code == 200
    assert response.json() == {"result": 42}

def test_addition_invalid_data():
    response = client.post("/add", json={"numbers": ["a", "b", "c"]})
    assert response.status_code == 422
