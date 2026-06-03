from pydantic import BaseModel
class PatientCreate(BaseModel):
    name: str
    email: str       # <-- This was missing!
    phone: str
    age: int
    gender: str
    blood_group: str
    medical_condition: str