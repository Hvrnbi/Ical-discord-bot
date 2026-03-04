### IMPORTS ###

# Discord #
import discord
from discord.ext import commands
from discord import app_commands

# For env variables #
from os import environ
from dotenv import load_dotenv

# Other #
from typing import Literal

# Commands #
from day_planning import today, tomorrow


### BOT CLASS ###

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = "?", intents = intents)

    async def setup_hook(self):
        await self.tree.sync(guild= discord.Object(id=guild))
        print("Bot started")

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)


### VARIABLES ###

load_dotenv()
token = environ["TOKEN"]
guild = environ["GUILD"]

bot = Bot()


### COMMANDS ###

@bot.hybrid_command(name="day", with_app_command=True, description="Give your attends for one day")
@app_commands.guilds(discord.Object(id=guild))
@app_commands.describe(date="The day for which your attends will be displayed")
async def day(ctx, date: Literal["today", "tomorrow"]):

    if date == "today":
        msg = today()

    elif date == "tomorrow":
        msg = tomorrow()
    
    else:
        msg = "This date doesn't exist"

    await ctx.reply(msg)


bot.run(token)

