import pytest
from fastapi.testclient import TestClient
from app.main import app

# 1. THE FIXTURE
# This creates the robot once and injects it wherever requested
@pytest.fixture
def client():
    return TestClient(app)

# 2. THE REFACTOR
# We pass 'client' into the parentheses. 
# Delete the old 'client = TestClient(app)' from inside here!
def test_get_public_patients_api(client):
    response = client.get("/api/v1/patients")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
    if len(data) > 0:
        first_patient = data[0]
        assert "id" in first_patient
        assert "name" in first_patient
        assert "hashed_password" not in first_patient


# 3. POSITIVE TEST: Successful Login
def test_successful_login(client):
    # Simulating the HTML form data
    login_data = {"username": "BhanuAdmin", "password": "admin123"}
    
    # We must stop the robot from blindly following the redirect to catch the 303 status!
    response = client.post("/login", data=login_data, follow_redirects=False)
    
    # Assertions
    assert response.status_code == 303 
    assert response.headers["location"] == "/api/patients/web" 
    assert "access_token" in response.cookies


# 4. NEGATIVE TEST: Active Rejection
def test_failed_login(client):
    # Form data with a bad password
    bad_data = {"username": "BhanuAdmin", "password": "wrongpassword!"}
    
    # Send the POST request (no redirect blocking needed here)
    response = client.post("/login", data=bad_data)
    
    # Assertions
    assert response.status_code == 400 
    assert response.json()["detail"] == "Invalid Credentials"