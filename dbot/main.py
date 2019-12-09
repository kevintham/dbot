import os
import random
import requests

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('API_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = os.getenv('CHANNEL_ID')
FFLOGS_API_KEY = os.getenv('FFLOGS_API_KEY')

bot = commands.Bot(command_prefix='!')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='latest_parse',
             help="Pulls character's latest parse")
async def latest_parse(ctx, char_name: str, world: str, dc: str):
    char_name_parsed = char_name.replace(" ", "%20")
    url = "https://www.fflogs.com:443/v1/parses/character/" \
          "{CHAR_NAME}/{WORLD}/{DC}?api_key={FFLOGS_API_KEY}"\
        .format(FFLOGS_API_KEY=FFLOGS_API_KEY,
                WORLD=world,
                DC=dc,
                CHAR_NAME=char_name_parsed)
    r = requests.get(url)
    reports = r.json()
    timekeys = {i['startTime']: i for i in reports}
    latest_parse = timekeys[max(timekeys.keys())]
    await ctx.send(latest_parse)


bot.run(TOKEN)
