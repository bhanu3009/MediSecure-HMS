from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
import jwt
import os
from app.config.database import get_db
from app.models.staff_model import Staff
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")

def create_access_token(data):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(request: Request, db: Session = Depends(get_db)):
    """The Firewall Bouncer: Intercepts the request and cryptographically verifies the token."""
    token = request.cookies.get("access_token")
    
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER, 
            headers={"Location": "/login"}
        )

    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
        user_id = payload.get("sub")
        
        user = db.query(Staff).filter(Staff.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, headers={"Location": "/login"})
            
        return user # Security cleared. Let them in.
        
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, headers={"Location": "/login"})
    

class RoleChecker:
    """The VIP Guard: A dynamic dependency to enforce strict Role-Based Access Control."""
    
    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user = Depends(get_current_user)):
        # Check if the user's role is in the cleared list
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation forbidden. Insufficient clearance."
            )
        return current_user