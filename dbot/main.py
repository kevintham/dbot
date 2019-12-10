import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('API_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = commands.Bot(command_prefix='!')
bot.load_extension("cogs.dice")
bot.load_extension("cogs.fflogs")
bot.run(TOKEN)
