from fastapi import APIRouter, Depends, HTTPException, Request, Form, BackgroundTasks
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
# ---> ADDED: PatientProfileUpdate imported here
from app.schemas.patient import PatientCreate, PatientUpdate, PatientProfileUpdate
from sqlalchemy.orm import Session
from datetime import datetime 
from app.models.patient import Patient
from app.config.database import get_db
from app.models.doctor_model import Doctor
from typing import Optional
from app.utils.auth import get_current_user, RoleChecker
from fastapi import File, UploadFile
import shutil
import os
from app.utils.email_service import send_welcome_email
from sqlalchemy.exc import IntegrityError

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
    current_user = Depends(get_current_user)  # <-- Bouncer
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
            "size": size,
            "current_user": current_user 
        }
    )

# 2. PROTECTED ADD ACTION (NOW WITH ASYNC EMAIL & ERROR HANDLING)
@router.post('/web/add', include_in_schema=False)
def add_patient_from_web(
    background_tasks: BackgroundTasks, 
    name: str = Form(...), 
    email: str = Form(...), 
    phone: str = Form(...), 
    primary_doctor_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_patient = Patient(
        name=name, 
        email=email.lower(), 
        phone=phone,
        age=0,              
        gender="Unknown",
        primary_doctor_id=primary_doctor_id,
    )
    
    try:
        db.add(new_patient)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Registration failed: A patient with this email already exists.")
    
    background_tasks.add_task(send_welcome_email, patient_name=name, patient_email=email.lower())
    return RedirectResponse(url="/api/patients/web", status_code=303)


# 3. HIGH-SECURITY DELETE ACTION (ADMIN ONLY)
@router.post('/web/{patient_id}/delete', include_in_schema=False)
def delete_patient_web(
    patient_id: int, 
    db: Session = Depends(get_db),
    admin_user = Depends(RoleChecker(["Admin"]))  
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
    current_user = Depends(get_current_user)
):
    patient_folder = db.query(Patient).filter(Patient.id == patient_id).first()
    return templates.TemplateResponse(
        request=request, 
        name="patient_edit.html", 
        context={"patient": patient_folder, "current_user": current_user}
    )

# 5. PROTECTED UPDATE ACTION
@router.post('/web/{patient_id}/edit',include_in_schema=False)
def update_patient_web(
    patient_id:int, 
    email:str=Form(...), 
    phone:str=Form(...), 
    profile_pic:UploadFile=File(None), 
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
):
    patient_folder=db.query(Patient).filter(Patient.id==patient_id).first()
    
    if patient_folder:
        patient_folder.email=email.lower()
        patient_folder.phone=phone
        
        if profile_pic and profile_pic.filename:
            safe_filename=f"patient_{patient_id}_{profile_pic.filename}"
            file_location=f"app/uploads/{safe_filename}"
            
            with open(file_location, "wb+") as file_object:
                shutil.copyfileobj(profile_pic.file, file_object)
            patient_folder.profile_picture_url=f"/uploads/{safe_filename}"
            
        db.commit()
        
    return RedirectResponse(url="/api/patients/web",status_code=303)


# --- Pure API JSON Endpoints ---

@router.get('/')
def get_all_patients(db: Session = Depends(get_db)):
    all_patients = db.query(Patient).all()
    return {
        "message": "Hospital roster successfully retrieved!",
        "total_patients": len(all_patients),
        "data": all_patients
    }

# ---> UPDATED STEP 4: Build the View API (Must be ABOVE /{patient_id})
@router.get('/profile')
def get_patient_profile(current_user = Depends(get_current_user)):
    """
    Fetches the profile of the currently logged-in patient using their JWT token.
    """
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Security Check: Ensure this is actually a patient!
    if getattr(current_user, "role", None) == "Admin" or hasattr(current_user, "username"):
        raise HTTPException(status_code=403, detail="Admins cannot have a patient profile.")
        
    # Strip sensitive fields before returning the data
    safe_profile = current_user.__dict__.copy()
    safe_profile.pop("hashed_password", None)
    
    return safe_profile

# ---> UPDATED STEP 5: Build the Update API
@router.patch('/profile')
def update_patient_profile(
    payload: PatientProfileUpdate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Securely updates the logged-in patient's medical history and contact info.
    """
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Security Check: Ensure this is actually a patient!
    if getattr(current_user, "role", None) == "Admin" or hasattr(current_user, "username"):
        raise HTTPException(status_code=403, detail="Admins cannot update a patient profile.")
        
    # Extract only the fields the user actually sent in the request
    update_data = payload.model_dump(exclude_unset=True)
    
    # Apply those specific fields to the database model
    for key, value in update_data.items():
        setattr(current_user, key, value)
        
    db.commit()
    db.refresh(current_user)
    
    # Strip sensitive fields before returning the data
    safe_profile = current_user.__dict__.copy()
    safe_profile.pop("hashed_password", None)
    
    return {
        "message": "Profile updated successfully", 
        "profile": safe_profile
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