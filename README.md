# 🧠 ZimaBlade Homelab Journey: From CasaOS to TrueNAS SCALE

## 📌 Introduction
This project documents the full transition and setup process of moving from **CasaOS** to **TrueNAS SCALE** on a **ZimaBlade** as a core homelab server. The setup is focused on achieving a reliable, modular, self-hosted infrastructure using Docker, ZFS, and secure remote access via Tailscale.

Arvan Jindam (me 🙋‍♂️), a data science student and homelab enthusiast, built this system to learn more about IT infrastructure, self-hosting, and cybersecurity while maximizing the power of a single-board x86 device.

---

## ⚙️ Hardware & Base System

### 📦 Device: ZimaBlade (32GB eMMC)
- **SSD**: 32GB eMMC 
- **RAM**: 16GB DDR4 SODIMM  
- **Network**: 1GbE LAN

### 🧪 Previous OS: CasaOS
- Lightweight, container-based OS  
- Great for beginners but limited in power-user flexibility

### 🚀 New OS: TrueNAS SCALE
- Debian-based NAS OS with Docker & KVM support  
- Full ZFS support  
- Built-in apps + Portainer + CLI goodness

---

## 🔄 Migration Process

### 🧹 Step 1: Clean Wipe
- Backed up all existing volumes from CasaOS using `rsync` to external SSDs  
- Formatted internal SSD + HDD during TrueNAS SCALE installation

### 💿 Step 2: Install TrueNAS SCALE
- Used Ventoy USB with TrueNAS SCALE ISO  
- Installed on internal SSD (`/dev/sda`) with `/mnt/ZimaTB` and `/mnt/Zima2TB` as primary pools

### 🔐 Step 3: Secure Access
- Enabled SSH with key-based login  
- Installed Tailscale:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --authkey <auth_key>
```

- Allowed remote access to TrueNAS via Tailscale IP

### 📂 Step 4: Shared Storage
- Created datasets:
  - `media/Movies`, `media/Photos`, `media/TVShows`
  - `services/configs`, `services/docker`
- SMB shares for Mac & Windows access  
- Time Machine backups for macOS enabled

---

## 🐳 Container Setup

### 📦 Base Stack
Using **Portainer** and `docker-compose`:
- NetData (monitoring)  
- Jellyfin (media server)  
- Immich (photo management)  
- Vaultwarden (Bitwarden alternative)  
- Nextcloud (private cloud)  
- Deluge + Radarr + Sonarr (download stack)

All mapped to `/mnt/ZimaTB/media` or `/mnt/Zima2TB/downloads`

### 🌐 Networking
- Created custom Docker networks (e.g., `tailscale_net`, `proxy_net`)  
- All containers routed through **Tailscale** using `--network container:tailscale` or bridge + routing

---

## 🧰 Services Dashboard
Set up **Homepage** dashboard to quickly view:
- TrueNAS health  
- Docker containers  
- Portainer access  
- Quick launch to Immich, Jellyfin, etc.

---

## 🛠️ Troubleshooting & Fixes
- **Deluge not saving to SMB share** → Fixed with correct UID/GID + bind mount permissions  
- **Tailscale not routing traffic** → Set up subnet routing + IP forwarding  
- **Netdata not binding** → Opened port in UFW and set trusted interface

---

## 🗂️ Filesystem Overview

```bash
/mnt/ZimaTB
├── media
│   ├── Movies
│   ├── Photos
│   ├── TVShows
├── services
│   ├── configs
│   └── docker
```

---

## 🧪 Lessons Learned
- TrueNAS SCALE is **crazy powerful**, but needs patience  
- ZFS snapshots are 🔥 for rollback safety  
- Tailscale is a **gamechanger** for secure remote access  
- Docker in TrueNAS SCALE is stable, but Portainer makes it 10x better

---

## 📚 Next Steps
- Setup Prometheus + Grafana for long-term metrics  
- Add GitHub Actions backup trigger  
- Automate Tailscale re-auth with cron  
- Run Discord bot for server alerts (work in progress 👀)

---

## 🙌 Credits
- Maintained by: [@ArvanJindam](https://github.com/arvanjindam)  
- Assistant AI: ChatGPT

> Feel free to fork, star, and contribute!

