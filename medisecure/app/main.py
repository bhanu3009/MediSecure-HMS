from app.routers import patient as patient_router
from datetime import datetime
from fastapi import FastAPI
from sqlalchemy import text
from app.config.database import SessionLocal

app=FastAPI(title="MediSecure Backend")

@app.get("/api/health")
async def check_system_health():
    db_status="Disconnected"
    log_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open("system_config.txt","r")as file:
            config_text=file.read().strip()
        system_mode="ACTIVE" if config_text=="ACTIVE" else "Degraded"
    except FileNotFoundError:
        system_mode="Offline-Config Missing"

    db_session=None
    try:
        db_session=SessionLocal()
        db_session.execute(text("SELECT 1"))
        db_status="Connected"
    except Exception as e:
        db_status=f"Disconnected-Error:{str(e)}"
    finally:
        if db_session:
            db_session.close()

    with open("db_connection_log.txt","a")as log_file:
        log_file.write(f"[{log_time}] DB Status:{db_status}\n")

    return{
        "system_name":"MediSecure Backend",
        "system_mode":system_mode,
        "database_status":db_status,
        "timestamp":log_time
    }
app.include_router(patient_router.router,prefix="/api/patients",tags=["Patients"])