import os
import random

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('API_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = commands.Bot(command_prefix='!')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
