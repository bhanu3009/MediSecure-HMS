from sqlalchemy import Column,Integer,String
from app.config.database import Base

class Staff(Base):
    __tablename__ ="staff"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,index=True,nullable=False)
    
    # Notice we do not have a 'password' column. We ONLY store the hash.
    hashed_password=Column(String(255),nullable=False)
    
    role=Column(String(50),default="Staff",nullable=False)