from fastapi import FastAPI
from datetime import datetime

app=FastAPI(title="Medical-secure")

@app.get("/api/health")

async def check_system_health():
    try:
        with open("system_config.txt", "r") as file:
            file = file.read().strip()

            if file== "ACTIVE":
             db_status = "Connected"
            else:
             db_status = "Degraded"
    except FileNotFoundError:
        db_status="Offline-Config Missing"

    current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return{
        "system_name":"MediSecure Backend",
        "status":db_status,
        "timestamp":current_time
    }