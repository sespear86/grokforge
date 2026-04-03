# src/monitoring/dashboard.py — FastAPI Production Dashboard (Phase 8)
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio
import json
from src.monitoring.auto_healing_monitor import AutoHealingMonitor

app = FastAPI(title="GrokForge Monitoring Dashboard")
templates = Jinja2Templates(directory="src/monitoring/templates")

healer = AutoHealingMonitor()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    status = await healer.get_live_status()
    status_json = json.dumps(status, indent=2)   # pre-rendered for safe template use
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "status": status,
        "status_json": status_json
    })

@app.get("/api/heal/{service}")
async def trigger_heal(service: str):
    result = await healer.heal_service(service)
    return {"service": service, "healed": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
