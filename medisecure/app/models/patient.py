from sqlalchemy import Column,Integer,String
from app.config.database import Base

class Patient(Base):
    __tablename__="patients"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    email = Column(String(100), unique=True, nullable=False) # <-- Added!
    phone = Column(String(20))
    age=Column(Integer,nullable=False)
    gender=Column(String(10),nullable=False)
    blood_group=Column(String(5))
    medical_condition=Column(String(255))