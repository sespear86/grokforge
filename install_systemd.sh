#!/bin/bash
# install_systemd.sh — Phase 7.3 safe user-level installer (no sudo)
set -e
echo "Installing GrokForge systemd services (user level — Fedora 43)"
mkdir -p ~/.config/systemd/user
cp systemd/*.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now grokforge-swarm.service
systemctl --user enable --now grok-dream.service
echo "✅ Services enabled and started. Check with: systemctl --user status grokforge-swarm"
