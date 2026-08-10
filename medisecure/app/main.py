import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import text
from pathlib import Path

from app.config.database import SessionLocal, Base, engine
from app.routers import patient as patient_router
from app.routers import doctor_router
from app.routers import auth_router
from app.routers import api_patient_router

app = FastAPI(title="MediSecure Backend | BP Studios")

# Base directory points to the 'app' folder where main.py lives
BASE_DIR = Path(__file__).resolve().parent

# Define absolute paths for templates and static files
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

os.makedirs("app/uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

# 2. ROUTER REGISTRATION
# Internal HTML Dashboards
app.include_router(patient_router.router, prefix="/api/patients", tags=["Patients"])
app.include_router(doctor_router.router)
app.include_router(auth_router.router)

# External JSON APIs
app.include_router(api_patient_router.router)

# 3. DATABASE INITIALIZATION
Base.metadata.create_all(bind=engine)

# 4. HEALTH CHECK ENGINE
@app.get("/api/health")
async def check_system_health():
    db_status = "Disconnected"
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open("system_config.txt", "r") as file:
            config_text = file.read().strip()
        system_mode = "ACTIVE" if config_text == "ACTIVE" else "Degraded"
    except FileNotFoundError:
        system_mode = "Offline-Config Missing"

    db_session = None
    try:
        db_session = SessionLocal()
        db_session.execute(text("SELECT 1"))
        db_status = "Connected"
    except Exception as e:
        db_status = f"Disconnected-Error:{str(e)}"
    finally:
        if db_session:
            db_session.close()

    with open("db_connection_log.txt", "a") as log_file:
        log_file.write(f"[{log_time}] DB Status:{db_status}\n")

    return {
        "system_name": "MediSecure Backend",
        "system_mode": system_mode,
        "database_status": db_status,
        "timestamp": log_time
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to MediSecure HMS API"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "MediSecure HMS API"
    }

# 5. UI ROUTES
@app.get("/ui/login", response_class=HTMLResponse)
async def show_login_ui(request: Request):
    # Updated for newest FastAPI version requirements
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"request": request}
    )