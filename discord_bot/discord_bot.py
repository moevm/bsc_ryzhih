import os
import discord
import nextcord
from event_manager import Events
from nextcord.ext import commands, ipc
from discord_manager import DiscordManager
from cogs.chat_history import send_email
from cogs.generate_message import message_text

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

def start():
    for extension in initial_extensions:
        client.load_extension(extension)
    client.ipc.start()
    client.run(DISCORD_BOT_TOKEN)


class DiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events = Events
        self.message_id = None
        self.roles = None
        self.ipc = ipc.Server(self, secret_key="secret1234", host="bot", port=8760, do_multicast=True)

    def track_message(self, message_id, roles):
        self.message_id = int(message_id)
        self.roles = roles.split(',')


    async def on_ready(self):
        print('We have successfully loggged in as {0.user}'.format(self))

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc is ready.")

    async def on_raw_reaction_add(self, payload):
        if self.message_id is None:
            return
        await DiscordManager.add_role_by_reaction(client=client, payload=payload, message_id=self.message_id, roles=self.roles)

    async def on_member_join(self, member):
        guild = self.get_guild(self.guild)
        await member.add_roles(discord.utils.get(guild.roles, name='2022'))


client = DiscordBot(intents=nextcord.Intents.all())
initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append('cogs.' + filename[:-3])


@client.ipc.route()
async def generate_message(data):
    channel_name = data.channel_name
    message_type = data.message_type
    repo_name = data.repo_name
    work = data.work

    testServerId = 1001473537451761664
    guild = client.get_guild(testServerId)
    for channel in guild.channels:
        if channel.name == channel_name:
            break

    response = await message_text(client, channel_name, message_type,
                                                               repo_name, work)

    return {response}  # return the member count to the client

@client.ipc.route()
async def chat_history(data):
    channel_name = data.channel_name
    email = data.email
    testServerId = 1001473537451761664
    guild = client.get_guild(testServerId)
    for channel in guild.channels:
        if channel.name == channel_name:
            break
    with open(channel.name + ".txt", "w+", encoding="utf-8") as file:
        messages = [message async for message in channel.history(oldest_first=True)]
        for message in messages:
            file.write(
                f"{message.created_at.strftime('%Y-%m-%d %H:%M:%S')} {message.author.display_name}: {message.content}\n")
        path = os.path.abspath(file.name)
        files = [path]
        file.close()  # Обязательно, т.к. без этого файл отправляется пустым
        send_email(email, "История чата", f"История чата {channel.name}:", files)

    return {'ok'}  # return the member count to the client

@client.ipc.route()
async def get_member_count(data):
    guild = client.get_guild(
        data.guild_id
    )  # get the guild object using parsed guild_id

    return guild.member_count  # return the member count to the client
