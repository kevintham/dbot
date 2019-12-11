import os
from datetime import datetime

import requests
import discord
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
        parsed_parse = self.parse_parse(latest_parse)
        await ctx.send(embed=parsed_parse)

    def parse_parse(self, parse_dict):

        name = parse_dict['characterName']
        ts = int(parse_dict['startTime'])//1000
        time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        bossname = parse_dict['encounterName']
        server = parse_dict['server']
        dps = parse_dict['total']
        perc = parse_dict['percentile']
        job = parse_dict['spec']

        embed = discord.Embed(title="{name}'s Latest Parse".format(name=name))
        embed.add_field(name="Server", value=server)
        embed.add_field(name="Job", value=job)
        embed.add_field(name="Date", value=time)
        embed.add_field(name="Encounter Name", value=bossname)
        embed.add_field(name="DPS", value=dps)
        embed.add_field(name="Percentile", value=perc)

        return embed


def setup(bot):
    bot.add_cog(Fflogs(bot))
