#!/bin/bash
# Tier 9 — UNIVERSAL Redis Bootstrap (Fedora 43 + Ubuntu + Debian + others)
echo "🔧 GrokDream Redis Full Universal Bootstrap (Tier 9)"

# Detect package manager
if command -v dnf >/dev/null 2>&1; then
    PKG_MANAGER="dnf"
    PKG_NAME="redis"
    echo "🧬 Detected Fedora/RHEL-based system (dnf)"
elif command -v apt >/dev/null 2>&1; then
    PKG_MANAGER="apt"
    PKG_NAME="redis-server"
    echo "🧬 Detected Debian/Ubuntu-based system (apt)"
else
    echo "❌ Unsupported package manager. Please install Redis manually."
    exit 1
fi

if command -v redis-server >/dev/null 2>&1; then
    echo "✅ redis-server already installed"
else
    echo "📦 Installing Redis via $PKG_MANAGER (requires sudo)..."
    if [ "$PKG_MANAGER" = "dnf" ]; then
        sudo dnf install -y "$PKG_NAME"
    else
        sudo apt update && sudo apt install -y "$PKG_NAME"
    fi
    if [ $? -ne 0 ]; then
        echo "❌ Install failed. Please run the command above manually."
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

echo "🎉 Redis is ready for GrokDream Daemon on your Fedora 43 system!"
