import discord
from discord import app_commands
from discord.ext import commands

from music.sources import YoutubeSource
from discord import FFmpegOpusAudio


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(query="Name or url of a song")
    @app_commands.command(
        name="play",
        description="TODO",
    )
    async def play(self, interaction: discord.Interaction, query: str):
        await interaction.response.send_message(f"Searching for {query}")

        # TODO: Check if whoever uses the command is in a channel
        # Get the voice channel where the user is connected
        channel = interaction.user.voice.channel

        # Get the voice client from the guild
        voice = interaction.guild.voice_client

        # If bot is not already connected to a channel connect it
        if not voice:
            voice = await channel.connect()

        # Get the audio from youtube
        source = YoutubeSource(query)
        voice.play(source)

        # Send what will be reproduced
        await interaction.followup.send(f"Playing {source.title}")


async def setup(bot: commands.Bot):
    # TODO: Automate guilds like in bot.py
    await bot.add_cog(Music(bot), guilds=[discord.Object(id=1050483093988970636)])
