from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientResponse

router = APIRouter(
    prefix="/api/v1/patients",
    tags=["Public API"]
)

@router.get("",response_model=List[PatientResponse])
def get_all_patients_api(db:Session=Depends(get_db)):
    patients=db.query(Patient).all()
    
    if not patients:
        raise HTTPException(status_code=404,detail="No patients found.")
        
    return patients