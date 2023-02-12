import os
import json
import discord
from github import Github
from discord import app_commands
from discord_manager import DiscordManager

TOKEN = os.environ.get('TOKEN')
TEST_TOKEN = os.environ.get('TEST_TOKEN')

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.presences = True


def start():
    client.run(TOKEN)


async def get_pulls(repo_name):
    g = Github(TEST_TOKEN)
    repo = g.get_user().get_repo(repo_name)
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    return pulls


async def generate_message(message_type):
    with open('settings.json', 'r', encoding='utf_8_sig') as f:
        settings = json.load(f)
    return settings["messages"][message_type]


class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False
        self.message_id = None
        self.roles = None

    def track_message(self, message_id, roles):
        self.message_id = int(message_id)
        self.roles = roles.split(',')

    async def on_ready(self):
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('We have successfully loggged in as {0.user}'.format(self))

    async def on_message(self, message):
        await DiscordManager.send_message(message=message, user=client.user)

    async def on_raw_reaction_add(self, payload):
        if self.message_id is None:
            return
        await DiscordManager.add_role_by_reaction(client=client, payload=payload, message_id=self.message_id, roles=self.roles)


client = DiscordBot()
tree = app_commands.CommandTree(client)

from slash_commands import *
