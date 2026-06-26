from pydantic import BaseModel,ConfigDict
from typing import Optional

class PatientCreate(BaseModel):
    name:str
    email:str     
    phone:str
    age:int
    gender:str
    blood_group:str
    medical_condition:str

class PatientUpdate(BaseModel):
    email: str
    phone: str

class PatientResponse(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    primary_doctor_id:Optional[int]=None
    profile_picture_url:Optional[str]=None
    
    model_config = ConfigDict(from_attributes=True)