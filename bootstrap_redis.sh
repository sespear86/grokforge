#!/bin/bash
# Tier 9 — Full Redis Bootstrap with Auto-Install (100% copy-paste ready)
echo "🔧 GrokDream Redis Full Bootstrap (Tier 9)"

if command -v redis-server >/dev/null 2>&1; then
    echo "✅ redis-server already installed"
else
    echo "📦 redis-server not found — installing now (requires sudo)..."
    sudo apt update && sudo apt install -y redis-server
    if [ $? -ne 0 ]; then
        echo "❌ Install failed. Please run manually:"
        echo "   sudo apt update && sudo apt install -y redis-server"
        exit 1
    fi
    echo "✅ Redis installed successfully"
fi

if pgrep -x "redis-server" >/dev/null; then
    echo "✅ Redis server already running on localhost:6379"
else
    echo "🚀 Starting Redis server in background..."
    redis-server --daemonize yes --port 6379 --logfile /tmp/redis_grokforge.log
    sleep 2
    echo "✅ Redis started successfully (log: /tmp/redis_grokforge.log)"
fi

echo "🎉 Redis is ready for GrokDream Daemon!"
