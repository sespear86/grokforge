#!/bin/bash
# Tier 10+ — Smart webhook launcher with auto venv detection (future-proof for any folder move)
echo "🌐 Starting GrokDream Webhook/API with smart venv detection..."
if [ -z "$VIRTUAL_ENV" ]; then
  echo "🔍 Auto-detecting venv..."
  # Try the exact path that just worked for you
  if [ -f "/home/Irikash/grokforge-palaces/mempalace-venv/bin/activate" ]; then
    source "/home/Irikash/grokforge-palaces/mempalace-venv/bin/activate"
    echo "✅ Activated known working venv"
  # Fallback to the longer path that appeared in your error log
  elif [ -f "/home/Irikash/AI_Projects/GrokForge/grokforge-palaces/mempalace-venv/bin/activate" ]; then
    source "/home/Irikash/AI_Projects/GrokForge/grokforge-palaces/mempalace-venv/bin/activate"
    echo "✅ Activated fallback venv"
  else
    echo "✅ Assuming already inside venv (no activation needed)"
  fi
else
  echo "✅ Already inside venv: $VIRTUAL_ENV"
fi
PYTHONPATH=. python grokdream_webhook.py
