# 🧠 Zimablade Homelab (Multi-Node)

This repository documents a Zimablade-based homelab that started as a CasaOS  TrueNAS SCALE migration and has grown into a multi-node Docker setup (docker-n1 + docker-n2), with reverse proxying, DNS filtering, home automation, backups, and security monitoring. [web:1]

##  Current architecture

### Nodes
- **docker-n1**: Core services + security (Wazuh), storage-backed apps (Nextcloud), secrets (Vaultwarden), DNS (AdGuard), backups/monitoring. [web:1]
- **docker-n2**: Edge + UI + automation (Nginx Proxy Manager, Homarr, Home Assistant, n8n), sync/backup utilities, secondary DNS + AdGuard sync. [web:1]

### Primary entrypoints
- Reverse proxy: Nginx Proxy Manager (docker-n2). [web:1]
- Dashboards: Homarr (docker-n2), Portainer agent on both nodes. [web:1]
- DNS: AdGuard Home (both nodes) + adguardhome-sync (docker-n2). [web:1]

##  Services by node

### docker-n1
- Wazuh: manager, indexer, dashboard. [web:1]
- AdGuard Home. [web:1]
- Vaultwarden. [web:1]
- Nextcloud + MariaDB + Redis. [web:1]
- Duplicati. [web:1]
- Glances. [web:1]
- CouchDB. [web:1]
- Portainer agent. [web:1]

### docker-n2
- Nginx Proxy Manager. [web:1]
- Home Assistant. [web:1]
- Homarr. [web:1]
- n8n. [web:1]
- Syncthing. [web:1]
- Speedtest Tracker. [web:1]
- WebDAV (Obsidian). [web:1]
- AdGuard Home + adguardhome-sync. [web:1]
- Crafty Controller. [web:1]
- Duplicati. [web:1]
- Glances. [web:1]
- Portainer agent. [web:1]
- status-bot. [web:1]

##  Storage notes

The original TrueNAS SCALE setup used pools like `/mnt/ZimaTB` and `/mnt/Zima2TB` with datasets for `media/*` and `services/*`; that structure is still the mental model for how bind mounts are organized (media vs configs vs downloads). [web:1]

##  Repo layout
- `README.md`: High-level overview (this file). [web:1]
- `Zimablade-HomeLab/`: Notes + compose examples. [web:1]

##  Next steps
- Add per-node `docker-compose.yml` (sanitized) and/or Portainer stack exports. [web:1]
- Document DNS strategy (primary/secondary), NPM hostnames, and backup targets. [web:1]
- Add monitoring/alerting (Prometheus/Grafana or similar). [web:1]
