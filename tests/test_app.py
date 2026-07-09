from app.app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    
    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "User Management API"

    assert data["status"] == "running"

    assert data["version"] == "1.0"
