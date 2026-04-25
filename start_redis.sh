#!/bin/bash
# Tier 9 — Redis Bootstrap Helper (100% copy-paste ready)
echo "🔧 GrokDream Redis Bootstrap (Tier 9)"

if command -v redis-server >/dev/null 2>&1; then
    if pgrep -x "redis-server" >/dev/null; then
        echo "✅ Redis server already running on localhost:6379"
    else
        echo "🚀 Starting Redis server in background..."
        redis-server --daemonize yes --port 6379 --logfile /tmp/redis_grokforge.log
        sleep 2
        echo "✅ Redis started successfully (log: /tmp/redis_grokforge.log)"
    fi
else
    echo "❌ redis-server command not found."
    echo "   Quick install (Ubuntu/Debian): sudo apt update && sudo apt install -y redis-server"
    echo "   Then run this script again."
    exit 1
fi
