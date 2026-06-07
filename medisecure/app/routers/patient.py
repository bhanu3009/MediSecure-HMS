from fastapi import APIRouter, Depends
from datetime import datetime 
from app.schemas.patient import PatientCreate
from app.models.patient import Patient
from app.config.database import get_db

router = APIRouter()

@router.post('/')
def create_patient(patient_data: PatientCreate,db: Session=Depends(get_db)):
    try:
        new_patient = Patient(
            name=patient_data.name,
            email=patient_data.email.lower(), 
            phone=patient_data.phone,
            age=patient_data.age,
            gender=patient_data.gender,
            blood_group=patient_data.blood_group,
            medical_condition=patient_data.medical_condition
        )
        db.add(new_patient)        
        db.commit()                
        db.refresh(new_patient)      
        return {
            "message": "Patient registration successfully saved to MySQL!",
            "patient_id": new_patient.id,
            "name": new_patient.name
        }
    except Exception as e:
        return {"error": f"Database Error: {str(e)}"}