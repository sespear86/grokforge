# src/monitoring/dashboard.py — FastAPI Production Dashboard (Phase 8 — simplified)
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import asyncio
import json
from src.monitoring.auto_healing_monitor import AutoHealingMonitor

app = FastAPI(title="GrokForge Monitoring Dashboard")

healer = AutoHealingMonitor()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GrokForge — Live Monitoring Dashboard</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #0f0f0f; color: #0f0; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { color: #0f0; text-align: center; }
        .card { background: #1a1a1a; border: 1px solid #0f0; border-radius: 8px; padding: 20px; margin: 20px 0; }
        pre { background: #111; padding: 15px; border-radius: 4px; overflow: auto; color: #0f0; white-space: pre-wrap; }
        button { background: #0f0; color: #000; border: none; padding: 12px 24px; border-radius: 4px; cursor: pointer; margin: 5px; font-size: 1rem; }
        button:hover { background: #ff0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 GrokForge Production Dashboard</h1>
        <div class="card">
            <h2>Live Services Status</h2>
            <pre>{status_json}</pre>
        </div>
        <div style="text-align:center; margin-top:30px;">
            <button onclick="location.reload()">🔄 Refresh Status</button>
            <button onclick="fetch('/api/heal/grokforge-swarm').then(r=>r.json()).then(console.log);location.reload()">Heal Swarm</button>
            <button onclick="fetch('/api/heal/grok-dream').then(r=>r.json()).then(console.log);location.reload()">Heal Dream</button>
        </div>
    </div>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    status = await healer.get_live_status()
    status_json = json.dumps(status, indent=2)
    return HTML_TEMPLATE.format(status_json=status_json)

@app.get("/api/heal/{service}")
async def trigger_heal(service: str):
    result = await healer.heal_service(service)
    return {"service": service, "healed": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
