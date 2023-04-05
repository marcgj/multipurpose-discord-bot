import discord
from discord import app_commands
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="github",
        description="Show bot's github")
    async def github(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"https://github.com/marcgj/multipurpose-discord-bot")


async def setup(bot: commands.Bot):
    # TODO: Automate guilds like in bot.py
    await bot.add_cog(Basic(bot), guilds=[discord.Object(id=1050483093988970636)])
