from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from app.config.database import get_db
from app.models.doctor_model import Doctor
from app.utils.auth import get_current_user

# We set the prefix to keep your URLs clean and organized
router = APIRouter(prefix="/doctors", tags=["Doctors"])
templates = Jinja2Templates(directory="app/templates")

# 1. THE MASTER VIEW: List all doctors
@router.get("/")
def get_doctors_list(
    request: Request, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) 
):
    doctors_list = db.query(Doctor).all()
    return templates.TemplateResponse(
        request=request,
        name="doctor_list.html",
        context={
            "request": request, 
            "doctors": doctors_list,
            "current_user": current_user 
        }
    )

# 2. THE DETAIL VIEW: Show one doctor and their assigned patients
@router.get('/{doctor_id}')
def get_doctor_profile(request: Request, doctor_id: int, db: Session = Depends(get_db)):
    target_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    
    # 404 Protection
    if not target_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found in the system.")
        
    # FIX: Explicitly assigning request, name, and context variables
    return templates.TemplateResponse(
        request=request,
        name="doctor_profile.html", 
        context={"request": request, "doctor": target_doctor}
    )