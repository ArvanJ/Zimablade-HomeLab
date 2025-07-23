# ⚙️ ZimaBlade Node Overview

This is my main ZimaBlade-powered Docker node — a compact, power-efficient server running 24/7 to host media apps, VPN access, reverse proxy tooling, and more. It complements my other nodes (`nodehaus1`, `nodehaus2`) in the homelab.

---

## 🚀 What's Running on the ZimaBlade

| Container              | Port(s)                         | Purpose |
|------------------------|----------------------------------|---------|
| **Jellyfin**           | 8096 → 30013                    | Media server to stream movies/TV from local drives |
| **Radarr**             | 7878                            | Auto-download movies via torrent/NZB |
| **Sonarr**             | — (Failed/Exited)               | Auto-download TV shows (not currently working) |
| **Bazarr**             | —                               | Adds subtitles to Radarr/Sonarr media |
| **Jellyseerr**         | 5055                            | Request manager UI for Jellyfin content |
| **DelugeVPN**          | —                               | Deluge torrent client w/ VPN built-in (restarting) |
| **Photoprism**         | 20800                           | Photo gallery + AI sorting/self-hosted Google Photos alt |
| **Jackett**            | — (Created, not running)        | Scrapes torrent sites for Sonarr/Radarr (not running yet) |
| **OpenVPN-AS**         | 943 (web), 1194 (UDP)           | VPN server to access your network remotely |
| **Tailscale Gateway**  | — (Restarting)                  | Exit node / subnet router for Zero Trust network access |
| **Tailscale VPN**      | — (Healthy)                     | Peer-to-peer VPN across all your homelab devices |
| **Netdata**            | 20489                           | Full stack monitoring + metrics dashboard |
| **Portainer Agent**    | 9001                            | Enables Portainer UI to manage containers remotely |
| **Portainer UI (EE)**  | 31015 → 9000                    | Docker container manager in the browser |
| **Watchtower**         | 8080 (Exited)                   | Auto-updates containers (currently not active) |
| **WebDAV Server**      | — (Restarting)                  | Web-based file share for Obsidian sync |
| **Permissions Scripts**| —                               | Used to fix Docker volume/user permission issues |

---

## 🔧 Why ZimaBlade?

- 🖥️ **Always-on Media Server** — Serves Jellyfin, Radarr/Sonarr, Photoprism
- 🌐 **Remote Access Node** — Runs Tailscale & OpenVPN
- 🔍 **Monitoring** — Uses Netdata + Portainer for insight
- 📦 **Storage Hub** — Mounted to large HDDs via TrueNAS SCALE
- 🧪 **Experimental Stuff** — Jackett, Watchtower, WebDAV, etc.

---

## 📦 Pro Tips

- All volumes are mapped to `/mnt/ZimaTB/` via TrueNAS SCALE
- Tailscale connects this node securely to the rest of the homelab
- Netdata gives you a full breakdown of resource usage in real-time
- Jellyseerr + Radarr + Deluge + VPN = full automated movie pipeline
- Keep an eye on `sonarr`, `delugevpn`, and `watchtower` — they're unstable

---

## 🧠 Future Upgrades

- Replace DelugeVPN with qBittorrent in a container
- Reverse proxy w/ Traefik or Caddy for better HTTPS UX
- Add Jellyfin subtitle automation via `autosubs`
- Move WebDAV to Caddy or Nginx for better reliability

---

If you’re reading this and trying to build something similar — just ping me and I’ll drop the compose files 🔧
