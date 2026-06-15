from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas.patient import PatientCreate, PatientUpdate
from sqlalchemy.orm import Session
from datetime import datetime 
from app.models.patient import Patient
from app.config.database import get_db
from app.models.doctor_model import Doctor
from typing import Optional
from app.utils.auth import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# 1. PROTECTED MAIN DASHBOARD
@router.get('/web', include_in_schema=False)
def show_patient_webpage(
    request: Request, 
    search: Optional[str] = None, 
    page: int = 1, 
    size: int = 10, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # <-- Bouncer Added Here
):
    query = db.query(Patient)
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(Patient.name.ilike(search_term))
        
    total_records = query.count()
    total_pages = (total_records + size - 1) // size 
    if total_pages == 0: 
        total_pages = 1 
        
    offset = (page - 1) * size
    all_patients = query.offset(offset).limit(size).all()
    all_doctors = db.query(Doctor).all() 
    
    return templates.TemplateResponse(
        request=request, 
        name="patient_list.html", 
        context={
            "request": request,
            "hospital_name": "MediSecure Main Branch", 
            "patients": all_patients,
            "doctors": all_doctors,
            "search_query": search,
            "current_page": page,       
            "total_pages": total_pages, 
            "size": size                
        }
    )

# 2. PROTECTED ADD ACTION
@router.post('/web/add', include_in_schema=False)
def add_patient_from_web(
    name: str = Form(...), 
    email: str = Form(...), 
    phone: str = Form(...), 
    primary_doctor_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # <-- Bouncer Added Here
):
    new_patient = Patient(
        name=name, 
        email=email.lower(), 
        phone=phone,
        age=0,              
        gender="Unknown",
        primary_doctor_id=primary_doctor_id,
    )
    
    db.add(new_patient)
    db.commit()
    return RedirectResponse(url="/api/patients/web", status_code=303)

# 3. PROTECTED DELETE ACTION
@router.post('/web/{patient_id}/delete', include_in_schema=False)
def delete_patient_web(
    patient_id: int, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # <-- Bouncer Added Here
):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if patient_folder:
        db.delete(patient_folder)
        db.commit()
        
    return RedirectResponse(url="/api/patients/web", status_code=303)

# 4. PROTECTED EDIT PAGE
@router.get('/web/{patient_id}/edit', include_in_schema=False)
def show_edit_page(
    patient_id: int, 
    request: Request, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # <-- Bouncer Added Here
):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    return templates.TemplateResponse(
        request=request, 
        name="patient_edit.html", 
        context={"patient": patient_folder}
    )

# 5. PROTECTED UPDATE ACTION
@router.post('/web/{patient_id}/edit', include_in_schema=False)
def update_patient_web(
    patient_id: int, 
    email: str = Form(...), 
    phone: str = Form(...), 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # <-- Bouncer Added Here
):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if patient_folder:
        patient_folder.email = email.lower()
        patient_folder.phone = phone
        db.commit()
        
    return RedirectResponse(url="/api/patients/web", status_code=303)


# --- Pure API JSON Endpoints (Kept Unchanged for Background Requests) ---

@router.get('/')
def get_all_patients(db: Session = Depends(get_db)):
    all_patients = db.query(Patient).all()
    return {
        "message": "Hospital roster successfully retrieved!",
        "total_patients": len(all_patients),
        "data": all_patients
    }

@router.get('/{patient_id}')
def get_single_patient(patient_id: int, db: Session = Depends(get_db)):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient_folder:
        raise HTTPException(status_code=404, detail="Patient record not found in MySQL.")
    return patient_folder

@router.post('/')
def create_patient(patient_data: PatientCreate, db: Session = Depends(get_db)):
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
def update_patient(patient_id: int, update_data: PatientUpdate, db: Session = Depends(get_db)):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient_folder:
        raise HTTPException(status_code=404, detail="Patient not found.")
    
    patient_folder.email = update_data.email.lower()
    patient_folder.phone = update_data.phone
    
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