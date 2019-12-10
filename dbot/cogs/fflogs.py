import os

import requests
from discord.ext import commands
from discord.ext.commands import Cog
from dotenv import load_dotenv


class Fflogs(Cog):

    def __init__(self, bot):
        load_dotenv()
        self.bot = bot
        self.FFLOGS_API_KEY = os.getenv('FFLOGS_API_KEY')

    @commands.command(name='latest_parse')
    async def latest_parse(self, ctx, char_name: str, world: str, dc: str):
        """Pulls character's latest parse."""
        char_name_parsed = char_name.replace(" ", "%20")
        url = "https://www.fflogs.com:443/v1/parses/character/" \
              "{CHAR_NAME}/{WORLD}/{DC}?api_key={FFLOGS_API_KEY}"\
            .format(FFLOGS_API_KEY=self.FFLOGS_API_KEY,
                    WORLD=world,
                    DC=dc,
                    CHAR_NAME=char_name_parsed)
        r = requests.get(url)
        reports = r.json()
        timekeys = {i['startTime']: i for i in reports}
        latest_parse = timekeys[max(timekeys.keys())]
        await ctx.send(latest_parse)


def setup(bot):
    bot.add_cog(Fflogs(bot))
