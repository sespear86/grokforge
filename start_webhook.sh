#!/bin/bash
# Tier 10 — Webhook/API Server Launcher (CORRECTED path for your exact setup)
echo "🌐 Starting GrokDream Webhook/API with correct venv..."
source /home/Irikash/grokforge-palaces/mempalace-venv/bin/activate
PYTHONPATH=. python grokdream_webhook.py
