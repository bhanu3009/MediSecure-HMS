from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.staff_model import Staff
from app.utils.security import verify_password
from app.utils.auth import create_access_token

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get('/login', include_in_schema=False)
def show_login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={"request": request})

@router.post('/login', include_in_schema=False)
def process_login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    
    # Step A: Find the user in the database
    user = db.query(Staff).filter(Staff.username == username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    # Step B: Pass the inputs into your cryptographic blender
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    # Step C: Generate the Digital Wristband (JWT)
    token_data = {"sub": str(user.id)}
    token = create_access_token(token_data)

    # Step D: Plant the HttpOnly Cookie and Redirect to the Command Center
    response = RedirectResponse(url="/api/patients/web", status_code=303)
    response.set_cookie(key="access_token", value=token, httponly=True)

    return response