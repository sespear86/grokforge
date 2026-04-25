#!/bin/bash
# Tier 10 — TRUE 24/7 Launcher (background + auto-restart on crash)
echo "🚀 Starting GrokDream Daemon in TRUE 24/7 mode..."
./bootstrap_redis.sh
while true; do
    PYTHONPATH=. python grokdream_daemon.py --continuous --sleep 30
    echo "⚠️  Daemon stopped unexpectedly — self-healing restart in 5 seconds..."
    sleep 5
done
