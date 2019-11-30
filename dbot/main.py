import discord


client = discord.Client()
token='NjUwMzY4ODc4MjUzNDQxMDI0.XeKVTg.I-0yIhCgCMX7eAvx6qbDHGfhFQE'
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)