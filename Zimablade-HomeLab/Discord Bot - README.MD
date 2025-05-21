# 🖥️ Discord Server Monitor Bot

A self-hosted Discord bot to monitor your Linux server (Proxmox, Ubuntu, etc.) directly from a Discord channel — complete with interactive buttons!

## 🚀 Features
- Live server stats (CPU, RAM, Disk)
- Buttons to Refresh, Shutdown, Reboot
- `/status` command for on-demand check

## 📦 Requirements
- Python 3.8+
- A Discord bot token
- `psutil`, `discord.py`, `dotenv`

## 📖 Usage

```bash
git clone https://github.com/YOUR_USERNAME/discord-server-monitor.git
cd discord-server-monitor
pip install -r requirements.txt
cp .env.example .env
# Put your bot token in .env
python bot.py



---

### ⚡ Final Tip
- Use `discord_app_commands` if you want fancy `/slash` commands.
- You can expand with Docker stats, GPU temp, etc.

Want me to:
- Push this to a GitHub repo for you?
- Add more buttons like **“Restart container”**, **“Check Netdata alerts”**, etc.?

Just say the word 👇
