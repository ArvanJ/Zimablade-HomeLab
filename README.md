<!-- Badges -->
[![CI](https://github.com/OWNER/REPO/actions/workflows/WORKFLOW_FILE.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/WORKFLOW_FILE.yml)
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](./LICENSE)
[![Discord](https://img.shields.io/discord/DISCORD_SERVER_ID?logo=discord)](https://discord.gg/58DrHBFrgU)

# Homelab (Multi-Node)

This repository documents a Zimablade-based homelab that started as a CasaOS -> TrueNAS SCALE migration and has grown into a multi-node Docker setup (docker-n1 + docker-n2), with reverse proxying, DNS filtering, home automation, backups, and security monitoring.

## Current architecture

### Nodes
- docker-n1: Core services + security (Wazuh), storage-backed apps (Nextcloud), secrets (Vaultwarden), DNS (AdGuard), backups/monitoring.
- docker-n2: Edge + UI + automation (Nginx Proxy Manager, Homarr, Home Assistant, n8n), sync/backup utilities, secondary DNS + AdGuard sync.

### Primary entrypoints
- Reverse proxy: Nginx Proxy Manager (docker-n2).
- Dashboards: Homarr (docker-n2), Portainer agent on both nodes.
- DNS: AdGuard Home (both nodes) + adguardhome-sync (docker-n2).

## Services by node

### docker-n1
- Wazuh: manager, indexer, dashboard.
- AdGuard Home.
- Vaultwarden.
- Nextcloud + MariaDB + Redis.
- Duplicati.
- Glances.
- CouchDB.
- Portainer agent.

### docker-n2
- Nginx Proxy Manager.
- Home Assistant.
- Homarr.
- n8n.
- Syncthing.
- Speedtest Tracker.
- WebDAV (Obsidian).
- AdGuard Home + adguardhome-sync.
- Crafty Controller.
- Duplicati.
- Glances.
- Portainer agent.
- status-bot.

## Storage notes

The original TrueNAS SCALE setup used pools like `/mnt/ZimaTB` and `/mnt/Zima2TB` with datasets for `media/*` and `services/*`; that structure is still the mental model for how bind mounts are organized (media vs configs vs downloads).

## Repo layout
- README.md: High-level overview (this file).
- Zimablade-HomeLab/: Notes + compose examples.

## Next steps
- Add per-node docker-compose.yml (sanitized) and/or Portainer stack exports.
