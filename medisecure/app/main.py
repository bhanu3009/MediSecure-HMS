from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from datetime import datetime
import os

from app.config.database import SessionLocal, Base, engine
from app.routers import patient as patient_router
from app.routers import doctor_router
from app.routers import auth_router
from app.routers import api_patient_router

app = FastAPI(title="MediSecure Backend | BP Studios")

# 1. FILE SYSTEM MOUNTS (Grouped together)
os.makedirs("app/uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
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