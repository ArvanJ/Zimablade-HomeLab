# 🧰 ZimaBlade Docker Homelab Stack

A self-hosted modular Docker setup for running all your homelab services — from automation to monitoring, DNS filtering, cloud storage, and more — powered by multiple containers across two nodes.

---

## 🚀 What’s Included

- 💾 **Nextcloud** — Personal cloud storage  
- 🧠 **n8n** — Visual automation workflows  
- 🏠 **Home Assistant** — Smart home controller  
- 🚫 **Pi-hole** — DNS ad-blocker  
- 📊 **Glances / CheckMK** — System monitoring  
- 📈 **Speedtest Tracker** — Logs your internet speeds  
- 🔒 **Wazuh Stack** — Security visibility, logs, agents  
- 📚 **Jupyter Notebook** — Python/Data science environment  
- 🧭 **Homepage** — Dashboard for all services  
- ☁️ **WebDAV Server** — Syncs Obsidian Markdown vault  
- 📦 **Portainer Agent** — Docker container management (used with Portainer UI)

---

## 🖥️ Node Summary

### `nodehaus1`

| Container             | Port(s)                | Role                     |
|-----------------------|------------------------|--------------------------|
| `pi-hole`             | 53, 67, 8088, 4443     | DNS filtering            |
| `nextcloud`           | 8884                   | Cloud storage            |
| `mariadb`             | 3306                   | Nextcloud DB             |
| `wazuh-manager`       | 1514–1515, 514, 55000  | SIEM manager             |
| `wazuh-indexer`       | 9200                   | Elasticsearch backend    |
| `wazuh-dashboard`     | 15601                  | Security dashboard       |
| `speedtest-tracker`   | 8765                   | Speed logging            |
| `jupyter-notebook`    | 8888                   | Python dev environment   |
| `portainer-agent`     | 9001                   | Remote container mgmt    |

---

### `nodehaus2`

| Container             | Port(s)                | Role                     |
|-----------------------|------------------------|--------------------------|
| `n8n`                 | 5678                   | No-code automations      |
| `obsidian-webdav`     | 8081                   | Sync notes w/ Obsidian   |
| `home-assistant`      | 8123                   | Home automation          |
| `pi-hole`             | 53, 67, 8088, 4443     | DNS filtering            |
| `checkmk`             | 5000, 6557             | System monitoring        |
| `glances`             | —                      | System stats             |
| `nebula-sync`         | —                      | Markdown sync agent      |
| `homepage`            | 3000                   | Web dashboard            |
| `speedtest-tracker`   | 8765                   | Speed logging            |
| `portainer-agent`     | 9001                   | Remote container mgmt    |

---

## 📦 Requirements

- Docker + Docker Compose  
- Tailscale (for remote admin access)  
- Public/private DNS setup (e.g. Cloudflare + DuckDNS)  
- Optional: Traefik or Caddy for HTTPS with Let's Encrypt

---

## ⚙️ Usage

```bash
git clone https://github.com/ArvanJ/Zimablade-HomeLab.git
cd Zimablade-HomeLab/docker-stacks
docker compose up -d
