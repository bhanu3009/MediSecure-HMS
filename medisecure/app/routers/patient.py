from fastapi import APIRouter
from datetime import datetime 
from app.schemas.patient import PatientCreate
router = APIRouter()
@router.post('/api/patients')
def create_patient(patient_data: PatientCreate):
    try:
        cleaned_email = patient_data.email.lower()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("registration_audit.txt", "a") as log_file:
            log_file.write(f"[{current_time}] - New Registration Request: {patient_data.name}, {cleaned_email}\n")
        return {
            "message": "Patient registration successfully processed!",
            "data": {
                "name": patient_data.name,
                "email": cleaned_email,
                "phone": patient_data.phone
            }
        }
    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}