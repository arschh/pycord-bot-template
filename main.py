import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# prefix command
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Ping is {round(bot.latency * 1000)}")

# slash command
@bot.slash_command(name='ping')
async def slash_ping(ctx):
    await ctx.respond(f"Pong! Ping is {round(bot.latency * 1000)}")

# let bot run
bot.run(os.environ["TOKEN"])