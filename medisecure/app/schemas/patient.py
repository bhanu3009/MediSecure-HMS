from pydantic import BaseModel
class PatientCreate(BaseModel):
    name:str
    email:str     
    phone:str
    age:int
    gender:str
    blood_group:str
    medical_condition:str

class PatientUpdate(BaseModel):
    email:str
    phone:str