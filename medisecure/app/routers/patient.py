from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_patient(patient_data:PatientCreate,db:Session=Depends(get_db)):
    
    new_patient = Patient(
        name=patient_data.name,
        age=patient_data.age,
        gender=patient_data.gender,
        blood_group=patient_data.blood_group,
        medical_condition=patient_data.medical_condition
    )
    
    db.add(new_patient)
    
    db.commit()
    
    db.refresh(new_patient)
    
    return new_patient