# src/monitoring/dashboard.py — FastAPI Production Dashboard (Phase 8 — FINAL & STABLE)
import sys
import os
import asyncio
import json
import traceback
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Make 'src' importable no matter how we launch the script
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

app = FastAPI(title="GrokForge Monitoring Dashboard")

# Lazy healer (prevents import-time crashes)
_healer = None
def get_healer():
    global _healer
    if _healer is None:
        from monitoring.auto_healing_monitor import AutoHealingMonitor
        _healer = AutoHealingMonitor()
    return _healer

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
        .error { color: #f66; border: 2px solid #f66; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 GrokForge Production Dashboard</h1>
        {content}
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
    try:
        healer = get_healer()
        status = await healer.get_live_status()
        status_json = json.dumps(status, indent=2)
        content = f'<div class="card"><h2>✅ Live Services Status</h2><pre>{status_json}</pre></div>'
        print("✅ Dashboard: Successfully retrieved live status")
    except Exception as e:
        error_html = f"<div class='card error'><h2>⚠ Dashboard Error in get_live_status()</h2><pre>{traceback.format_exc()}</pre></div>"
        content = error_html
        print("❌ Dashboard error caught:", str(e))
    # Safe replacement — ignores all curly braces in CSS/JS
    return HTML_TEMPLATE.replace("{content}", content)

@app.get("/api/heal/{service}")
async def trigger_heal(service: str):
    try:
        healer = get_healer()
        result = await healer.heal_service(service)
        return {"service": service, "healed": result}
    except Exception as e:
        print(f"❌ Heal error for {service}:", str(e))
        return {"service": service, "healed": False, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
