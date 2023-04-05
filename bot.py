import discord
from discord.ext import commands

import os

# Import commands outside this file
from commands.basic import Basic

# Load environs from .env file
from dotenv import load_dotenv
load_dotenv()


class Bot(commands.Bot):
    def __init__(self, prefix='!', intents=discord.Intents.all()):
        intents.message_content = True
        super().__init__(command_prefix=prefix, intents=intents)

    async def on_ready(self):
        print(f"{self.user.name} connected!")
        await self.load_extension("commands.basic")

        # TODO: Do this for a specific guild or multiples
        await bot.tree.sync(guild=discord.Object(id=1050483093988970636))


if __name__ == "__main__":
    bot = Bot()
    bot.run(os.getenv("API_KEY"))
