import discord
import psutil
import platform
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

class StatusView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🔄 Refresh", style=discord.ButtonStyle.primary)
    async def refresh(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=get_status(), view=self)

    @discord.ui.button(label="🔻 Shutdown", style=discord.ButtonStyle.danger)
    async def shutdown(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Shutting down server... 🛑", ephemeral=True)
        os.system("sudo shutdown now")

    @discord.ui.button(label="🔁 Reboot", style=discord.ButtonStyle.secondary)
    async def reboot(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Rebooting server... ♻️", ephemeral=True)
        os.system("sudo reboot")

def get_status():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    os_info = platform.system() + " " + platform.release()
    return (
        f"🖥️ **Server Status**\n"
        f"🧠 CPU: `{cpu}%`\n"
        f"💾 Memory: `{mem}%`\n"
        f"💽 Disk: `{disk}%`\n"
        f"🧱 OS: `{os_info}`"
    )

@bot.command()
async def status(ctx):
    await ctx.send(get_status(), view=StatusView())

bot.run(TOKEN)