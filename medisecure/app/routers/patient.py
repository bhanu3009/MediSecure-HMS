from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import datetime 
from app.schemas.patient import PatientCreate
from app.models.patient import Patient
from app.config.database import get_db

router = APIRouter()

@router.get('/')
def get_all_patients(db:Session=Depends(get_db)):
    all_patients=db.query(Patient).all()
    return {
        "message": "Hospital roster successfully retrieved!",
        "total_patients": len(all_patients),
        "data": all_patients
    }

@router.get('/{patient_id}')
def get_single_patient(patient_id:int,db:Session=Depends(get_db)):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient_folder:
        raise HTTPException(status_code=404,detail="Patient record not found in MySQL.")
    return patient_folder

@router.post('/')
def create_patient(patient_data:PatientCreate,db:Session=Depends(get_db)):
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