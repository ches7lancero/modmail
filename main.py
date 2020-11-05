from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
# we need members inyent too
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
  print("The bot is ready!")
  bot.load_extensions("cogs.onMessage")
  
bot.run(os.environ.get("TOKEN"))
