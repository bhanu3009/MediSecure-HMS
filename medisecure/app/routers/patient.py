from fastapi import APIRouter,Depends,HTTPException,Request
from app.schemas.patient import PatientCreate,PatientUpdate
from sqlalchemy.orm import Session
from datetime import datetime 
from fastapi.templating import Jinja2Templates
from app.schemas.patient import PatientCreate
from app.models.patient import Patient
from app.config.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get('/web', include_in_schema=False)
def show_patient_webpage(request: Request, db: Session = Depends(get_db)):
    all_patients = db.query(Patient).all()
    return templates.TemplateResponse(
        request=request, 
        name="patient_list.html", 
        context={
            "hospital_name": "MediSecure Main Branch", 
            "patients": all_patients
        }
    )

@router.get('/')
def get_all_patients(db:Session=Depends(get_db)):
    all_patients=db.query(Patient).all()
    return{
        "message": "Hospital roster successfully retrieved!",
        "total_patients":len(all_patients),
        "data":all_patients
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
    

@router.put('/{patient_id}')
def update_patient(patient_id:int,update_data:PatientUpdate,db:Session=Depends(get_db)):
    patient_folder=db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient_folder:
        raise HTTPException(status_code=404,detail="Patient not found.")
    
    patient_folder.email=update_data.email.lower()
    patient_folder.phone=update_data.phone
    
    db.commit()
    db.refresh(patient_folder)
    
    return {
        "message": "Patient contact info successfully updated!",
        "data": patient_folder
    }

@router.delete('/{patient_id}')
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient_folder:
        raise HTTPException(status_code=404, detail="Patient not found.")
    
    db.delete(patient_folder)
    db.commit() 
    return {"message": "Patient record permanently deleted."}


