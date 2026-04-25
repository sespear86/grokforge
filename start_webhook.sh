#!/bin/bash
# Tier 10 — Webhook/API Server Launcher (auto-activates mempalace-venv)
echo "🌐 Starting GrokDream Webhook/API with venv..."
source ~/AI_Projects/GrokForge/grokforge-palaces/mempalace-venv/bin/activate
PYTHONPATH=. python grokdream_webhook.py
