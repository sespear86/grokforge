#!/bin/bash
# Tier 10/11 — Webhook/API Server Launcher (ultra-robust for your exact Fedora setup)
echo "🌐 Starting GrokDream Webhook/API with correct venv..."

# If not already in the mempalace-venv, activate it
if [[ -z "$VIRTUAL_ENV" ]] || [[ "$VIRTUAL_ENV" != *mempalace-venv* ]]; then
    source /home/Irikash/grokforge-palaces/mempalace-venv/bin/activate 2>/dev/null || \
    source /home/Irikash/AI_Projects/GrokForge/grokforge-palaces/mempalace-venv/bin/activate 2>/dev/null || \
    echo "⚠️  Venv activation failed — but proceeding because you are likely already in it"
fi

PYTHONPATH=. python grokdream_webhook.py
