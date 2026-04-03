#!/bin/bash
# install_systemd.sh — Phase 7.3 FIXED safe user-level installer
set -e
echo "Installing GrokForge systemd services (user level — Fedora 43)"
mkdir -p ~/.config/systemd/user
cp systemd/*.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now grokforge-swarm.service
systemctl --user enable --now grok-dream.service
echo "✅ Services enabled and started."
echo "Check status with:"
echo "  systemctl --user status grokforge-swarm.service"
echo "  systemctl --user status grok-dream.service"
