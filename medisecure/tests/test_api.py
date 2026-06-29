from fastapi.testclient import TestClient
from app.main import app

# 1. Initialize the robot user
client = TestClient(app)

# 2. The Test Function
def test_get_public_patients_api():
    
    # Simulating a GET request to the public JSON API
    response = client.get("/api/v1/patients")
    
    # 3. The Assertions (The Demands)
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    # 4. Deep Validation: Prove the Data Firewall works!
    if len(data) > 0:
        first_patient = data[0]
        assert "id" in first_patient
        assert "name" in first_patient
        assert "hashed_password" not in first_patient