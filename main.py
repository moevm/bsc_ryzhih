import discord

TOKEN = 'MTA1MDU2Mzk5NzM2OTM3MjcyMw.GbWfLI.zWb-deGY8N9SBAp6YNtUoiJjCOvz-BfFWwpn1g'


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#client = discord.Client()


@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.display_name}!')

        return

    if message.content.lower() == 'bye':
        await message.channel.send(f'See you later, {message.author.display_name}!')

        return


client.run(TOKEN)
