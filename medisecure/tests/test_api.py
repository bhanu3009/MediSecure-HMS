from tests.conftest import TestingSessionLocal
from app.models.staff_model import Staff
from passlib.context import CryptContext

# Setup hashing for our fake test data
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from app.models.patient import Patient # Import your patient model!

def test_get_public_patients_api(client):
   # 1. SEED THE RAM DB: Inject a fake patient with ALL mandatory fields
    db = TestingSessionLocal()
    fake_patient = Patient(
        name="Test Patient", 
        email="test@patient.com", 
        phone="555-0000",
        age=30,             # <-- Added the mandatory age!
        gender="Male"       # <-- Added just in case it's also required
    )
    db.add(fake_patient)
    db.commit()
    db.close()
    
    # 2. ACT: Now when the robot asks, the API will find our fake patient!
    response = client.get("/api/v1/patients")
    
    # 3. ASSERT
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
    # We can safely test the first patient again since we know they exist!
    first_patient = data[0]
    assert "id" in first_patient
    assert "name" in first_patient
    assert "hashed_password" not in first_patient

def test_successful_login(client):
    # 1. SEED THE RAM DB: Inject a fake user directly into the temporary database
    db = TestingSessionLocal()
    secure_password = pwd_context.hash("robot123")
    fake_admin = Staff(username="TestRobot", hashed_password=secure_password, role="Admin")
    db.add(fake_admin)
    db.commit()
    db.close()
    
    # 2. ACT: Simulating the HTML form data
    login_data = {"username": "TestRobot", "password": "robot123"}
    response = client.post("/login", data=login_data, follow_redirects=False)
    
    # 3. ASSERT
    assert response.status_code == 303 
    assert "access_token" in response.cookies 

def test_failed_login(client):
    bad_data = {"username": "TestRobot", "password": "wrongpassword!"}
    response = client.post("/login", data=bad_data)
    
    assert response.status_code == 400 
    assert response.json()["detail"] == "Invalid Credentials"

def test_protected_dashboard(client):
    """The Ultimate Test: Breaching the Authentication Firewall"""
    
    # 1. Seed the Database
    db = TestingSessionLocal()
    secure_password = pwd_context.hash("secure123")
    fake_doctor = Staff(username="DrRobot", hashed_password=secure_password, role="Doctor")
    db.add(fake_doctor)
    db.commit()
    db.close()
    
    # 2. Log in to get the security cookie
    login_data = {"username": "DrRobot", "password": "secure123"}
    # By setting follow_redirects=True, the TestClient acts like a real browser
    # It logs in, gets the 303, grabs the cookie, and instantly navigates to the next page!
    response = client.post("/login", data=login_data, follow_redirects=True)
    
    # 3. Since the browser followed the redirect to the dashboard, it should succeed
    assert response.status_code == 200