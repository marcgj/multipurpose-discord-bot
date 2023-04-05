
# Load env variables from a .env
from interactions import Client, CommandContext
import os
from dotenv import load_dotenv
load_dotenv()

bot = Client(token=os.getenv("API_KEY"))


@bot.command(
    name="github",
    description="Show the github of the bot")
async def credits(ctx: CommandContext):
    await ctx.send("https://github.com/marcgj/multipurpose-discord-bot")

bot.start()
