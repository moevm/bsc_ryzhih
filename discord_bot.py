TOKEN = 'MTA1MDU2Mzk5NzM2OTM3MjcyMw.GN4jU8.9fZAnhUvmbYH2C-l426m8BlD-uNglbHoP62B3M'

import discord
from discord import app_commands
from discord_manager import DiscordManager

intents = discord.Intents.all()
intents.message_content = True

def start():
    client.run(TOKEN)


class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1031609704188739614))
            self.synced = True
        print('We have successfully loggged in as {0.user}'.format(self))

    async def on_message(self, message):
        await DiscordManager.send_message(message=message, user=client.user)

    async def on_raw_reaction_add(self, payload):
        await DiscordManager.add_role_by_reaction(client=client, payload=payload, message_id=1053040934671101983)

    async def on_member_join(self, member):
        guild = self.get_guild(1031609704188739614)
        await member.add_roles(discord.utils.get(guild.roles, name='2022'))


client = DiscordBot()
tree = app_commands.CommandTree(client)

import slash_commands


