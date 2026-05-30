from pydantic import BaseModel, Field
class PatientCreate(BaseModel):
    name:str
    age:int
    gender:str
    blood_group:str=Field(...,max_length=5,description="Blood group cannot exceed 5 characters")
    medical_condition:str