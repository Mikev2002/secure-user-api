from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import user as models

client = TestClient(app)

def clear_users():
    db = SessionLocal()
    db.query(models.User).delete()
    db.commit()
    db.close()

def test_register_user():
    clear_users()
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_register_duplicate_user():
    clear_users()
    # First registration
    client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })

    # Duplicate registration
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 400
