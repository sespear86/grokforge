#!/bin/bash
# GrokForge Production Installer — 24/7 systemd user service (full foresight, no limits, daemon-ready)
set -e
echo "=== GROKFORGE 24/7 SYSTEMD INSTALLER (PRODUCTION UPGRADE) ==="
USER_SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="$USER_SERVICE_DIR/grokdream.service"
CLI_BINARY="$HOME/.local/bin/grokforge"
mkdir -p "$USER_SERVICE_DIR"
cat > "$SERVICE_FILE" << 'EOT'
[Unit]
Description=GrokForge GrokDream Autonomous Agent (24/7 Production)
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/Irikash/AI_Projects/GrokForge/grokforge
ExecStart=/home/Irikash/.local/bin/grokforge dream --no-dry-run
Restart=always
RestartSec=3
Environment=PYTHONUNBUFFERED=1
Environment=PYTHONDONTWRITEBYTECODE=1
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
EOT
systemctl --user daemon-reload
systemctl --user stop grokdream.service || true
systemctl --user enable grokdream.service
systemctl --user start grokdream.service
systemctl --user status grokdream.service --no-pager
echo "✅ GrokForge is now running 24/7 as production systemd user service (CLI binary + daemon fixes)!"
echo "Monitor: systemctl --user status grokdream"
echo "Logs: journalctl --user -u grokdream -f"
