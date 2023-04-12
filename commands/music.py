import discord
from discord import app_commands
from discord.ext import commands

from music.track import YoutubeTrack
from music.manager import GuildMusicManager


class Music(commands.Cog):
    music_manager = None

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join", description="Joins the user voice channel")
    async def join(self, interaction: discord.Interaction):
        await self._join(interaction)

    async def _join(self, interaction: discord.Interaction):
        # Get the voice client from the guild
        voice = interaction.guild.voice_client

        # TODO: Check if whoever uses the command is in a channel
        # Get the voice channel where the user is connected
        channel = interaction.user.voice.channel

        # If bot is not already connected to a channel connect it
        if not voice:
            voice = await channel.connect()

        # Generate a music manager instance
        # !Intended for single guild use
        self.music_manager = GuildMusicManager(voice)

    @app_commands.describe(query="Name or url of a song")
    @app_commands.command(
        name="play",
        description="TODO",
    )
    async def play(self, interaction: discord.Interaction, query: str):
        await interaction.response.send_message(f"Searching for {query}")

        # Get the voice client from the guild
        voice = interaction.guild.voice_client

        # If bot is not already connected to a channel connect it
        if not voice:
            await self._join(interaction)

        # Get the audio from youtube
        track = YoutubeTrack(query)
        self.music_manager.process_track(track)
        # Send what will be reproduced
        await interaction.followup.send(f"Playing {track.title}")


async def setup(bot: commands.Bot):
    # TODO: Automate guilds like in bot.py
    await bot.add_cog(Music(bot), guilds=[discord.Object(id=1050483093988970636)])
