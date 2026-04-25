#!/bin/bash
# Tier 10 — Continuous 24/7 GrokDream Daemon Launcher
echo "🚀 Starting GrokDream Daemon v5.3 in continuous mode (24/7 self-improving)..."
echo "   Palace will keep growing forever. Ctrl+C to stop gracefully."
./bootstrap_redis.sh
PYTHONPATH=. python grokdream_daemon.py --continuous --sleep 30
