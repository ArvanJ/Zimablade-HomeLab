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

## Repo contents

### Stacks directory tree

Below is the current `stacks/` layout (from `tree -l`).

```text
.
├── Adguard
│   ├── confdir
│   │   └── AdGuardHome.yaml
│   ├── docker-compose.yml
│   └── workdir
│       └── data
│           ├── filters
│           │   └── 1.txt
│           ├── sessions.db
│           └── stats.db
├── Adguard-Sync
│   ├── config
│   │   └── adguardhome-sync.yaml
│   └── docker-compose.yml
├── Checkmk-Glances
│   └── docker-compose.yml
├── duplicati
│   ├── config
│   │   ├── backup Duplicati-server 20251129115921.sqlite
│   │   ├── control_dir_v2
│   │   │   └── lock_v2
│   │   ├── Duplicati-server.sqlite
│   │   ├── installation.txt
│   │   └── machineid.txt
│   └── docker-compose.yml
├── filebeat-8.13.4-amd64.deb
├── filebrowser
│   ├── docker-compose.yml
│   ├── filebrowser.db
│   └── settings.json
├── glances
│   └── docker-compose.yml
├── graylog
│   ├── mongo_data
│   │   ├── _mdb_catalog.wt
│   │   ├── collection-0--3901917761755299417.wt
│   │   ├── collection-2--3901917761755299417.wt
│   │   ├── collection-4--3901917761755299417.wt
│   │   ├── diagnostic.data
│   │   │   ├── metrics.2025-06-30T15-12-29Z-00000
│   │   │   └── metrics.interim
│   │   ├── index-1--3901917761755299417.wt
│   │   ├── index-3--3901917761755299417.wt
│   │   ├── index-5--3901917761755299417.wt
│   │   ├── index-6--3901917761755299417.wt
│   │   ├── journal
│   │   │   ├── WiredTigerLog.0000000001
│   │   │   ├── WiredTigerPreplog.0000000001
│   │   │   └── WiredTigerPreplog.0000000002
│   │   ├── mongod.lock
│   │   ├── sizeStorer.wt
│   │   ├── storage.bson
│   │   ├── WiredTiger
│   │   ├── WiredTiger.lock
│   │   ├── WiredTiger.turtle
│   │   ├── WiredTiger.wt
│   │   └── WiredTigerHS.wt
│   └── os_data
├── headscale
│   ├── certs
│   ├── config
│   │   └── config.yaml
│   ├── data
│   └── docker-compose.yml
├── homarr
│   ├── docker-compose.yml
│   └── homarr
│       └── appdata
│           ├── db
│           │   └── db.sqlite
│           ├── redis
│           │   └── dump.rdb
│           └── trusted-certificates
│               └── truenas_default.crt
├── home_assistant
│   ├── docker-compose.yml
│   └── homeassistant_config
│       ├── automations.yaml
│       ├── blueprints
│       │   ├── automation
│       │   │   └── homeassistant
│       │   │       ├── motion_light.yaml
│       │   │       └── notify_leaving_zone.yaml
│       │   └── script
│       │       └── homeassistant
│       │           └── confirmable_notification.yaml
│       ├── configuration.yaml
│       ├── deps
│       ├── home-assistant_v2.db
│       ├── home-assistant.log
│       ├── home-assistant.log.1
│       ├── scenes.yaml
│       ├── scripts.yaml
│       ├── secrets.yaml
│       └── tts
├── homepage
│   ├── config
│   │   ├── bookmarks.yaml
│   │   ├── custom.css
│   │   ├── custom.js
│   │   ├── docker.yaml
│   │   ├── kubernetes.yaml
│   │   ├── logs
│   │   │   └── homepage.log
│   │   ├── proxmox.yaml
│   │   ├── purpl1.png
│   │   ├── services.yaml
│   │   ├── settings.yaml
│   │   └── widgets.yaml
│   └── docker-compose.yml
├── Homey
│   └── docker-compose.yml
├── jupyter
├── minecraft_server
│   ├── banned-ips.json
│   ├── banned-players.json
│   ├── eula.txt
│   ├── libraries
│   │   └── (trimmed)
│   ├── logs
│   │   ├── 2025-12-15-1.log.gz
│   │   ├── 2025-12-15-2.log.gz
│   │   └── latest.log
│   ├── minecraft_server.1.21.11.jar
│   ├── ops.json
│   ├── server.properties
│   ├── start.sh
│   ├── usercache.json
│   ├── versions
│   │   └── 1.21.11
│   │       └── server-1.21.11.jar
│   ├── whitelist.json
│   └── world
│       └── (trimmed)
├── n8n
│   ├── binaryData
│   ├── config
│   ├── crash.journal
│   ├── database.sqlite
│   ├── database.sqlite-shm
│   ├── database.sqlite-wal
│   ├── docker-compose.yml
│   ├── git
│   ├── n8nEventLog-1.log
│   ├── n8nEventLog-2.log
│   ├── n8nEventLog.log
│   ├── nodes
│   │   └── package.json
│   └── ssh
├── netdata
│   └── docker-compose.yml
├── nginx
│   ├── data
│   │   ├── access
│   │   ├── custom_ssl
│   │   │   └── npm-5
│   │   │       ├── fullchain.pem
│   │   │       └── privkey.pem
│   │   ├── database.sqlite
│   │   ├── keys.json
│   │   ├── letsencrypt-acme-challenge
│   │   ├── logs
│   │   │   └── (trimmed)
│   │   └── nginx
│   │       ├── dead_host
│   │       ├── default_host
│   │       │   └── site.conf
│   │       ├── default_www
│   │       ├── proxy_host
│   │       │   └── (trimmed)
│   │       ├── redirection_host
│   │       ├── stream
│   │       └── temp
│   ├── docker-compose.yml
│   ├── letsencrypt
│   │   └── (trimmed)
│   └── mysql
│       └── (trimmed)
├── obsidian-couchdb
│   ├── data
│   ├── docker-compose.yml
│   └── local.ini
├── obsidian-vault
│   ├── couchdb_data
│   └── vault
│       ├── data
│       └── DavLock
├── rust
│   └── data
│       └── core.1
├── speedtest
│   └── docker-compose.yml
├── syncthing
│   ├── config
│   └── docker-compose.yml
├── vuln-scanner
│   ├── Dockerfile
│   ├── output
│   └── scan.sh
├── watchtower
│   ├── cache
│   ├── config
│   ├── docker-compose.yml
│   ├── index.html
│   └── ntfy
│       ├── data
│       └── server.yml
└── wazuh
    ├── docker-compose.yml
    └── multi-node
        ├── config
        │   └── wazuh_indexer_ssl_certs
        │       ├── root-ca.pem
        │       ├── wazuh-dashboard-key.pem
        │       └── wazuh-dashboard.pem
        ├── docker-compose.yml
        ├── generate-indexer-certs.yml
        └── instances.yml
```

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
- Document DNS strategy (primary/secondary), NPM hostnames, and backup targets.
- Add monitoring/alerting (Prometheus/Grafana or similar).
