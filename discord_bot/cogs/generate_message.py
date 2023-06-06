# Получение списка пул-реквестов
import os
import re
import json
import github
import nextcord
from nextcord.utils import get
from nextcord import Interaction
from nextcord.ext import commands, ipc

GIT_TOKEN = os.environ.get('GIT_TOKEN')
git = github.Github(GIT_TOKEN)


async def get_pulls(repo_name):
    repo = git.get_repo(repo_name)
    pulls = repo.get_pulls(state='open', sort='created')
    return pulls


async def get_message(message_type):
    with open('settings.json', 'r', encoding='utf_8_sig') as f:
        settings = json.load(f)
    return settings["messages"][message_type]


async def message_text(client, channel_name, message_type, repo_name, work):
    testServerId = 1001473537451761664
    guild = client.get_guild(testServerId)
    for channel in guild.channels:
        if channel.name == channel_name:
            break

    text = await get_message(message_type)
    text_begin, text_end = text.split('$people')
    pulls = await get_pulls(repo_name)
    mentions = ""
    work_number = None
    for pr in pulls:
        try:
            surname, name, work_type = re.findall('[^_]+', pr.title)
        except:
            return text_begin, pr.title, text_end, ''

        if work_type != work and work is not None:
            continue

        group = re.search('\d+', channel_name)
        if group is None:
            return text_begin, pr.title, text_end, group

        full_nick = surname + '.' + name + '.' + group[0]
        nick = full_nick.replace('ya', 'ja')
        # nick = translit(nick, 'ru')
        # -------------------------
        testServerId = 1001473537451761664
        guild = client.get_guild(testServerId)
        # -------------------------
        user = get(guild.members, nick=nick)

        if work:
            work_number = re.search('\d+', work)
            if work_number:
                work_number = work_number[0]

        if work_number:
            if user:
                mentions += '\n' + user.mention + f" -- Лабораторная работа номер {work_number}"
            else:
                mentions += '\n' + nick + f" -- Лабораторная работа номер {work_number}"
        elif work == 'cw':
            if user:
                mentions += '\n' + user.mention + f" -- Курсовая работа"
            else:
                mentions += '\n' + nick + f" -- Курсовая работа"
        else:
            if user:
                mentions += '\n' + user.mention + f" -- работа {work_type}"
            else:
                mentions += '\n' + nick + f" -- работа {work_type}"

    if group is None:
        return "You are not in the channel group!"
        # await interaction.response.send_message("You are not in the channel group!", ephemeral=True,
        #                                        delete_after=3.0)

    if len(mentions) == 0:
        return "No one has done this job"
        # await interaction.response.send_message("No one has done this job", ephemeral=True, delete_after=3.0)
        # return

    await channel.send(f"""
            {text_begin}
            {mentions}
            {text_end}
            """)
    return "Success!"


roles_list = ['Преподаватель', 'Модератор']


class GenerateMessage(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="generate_message", description="Generate message for students",
                            guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, message_type: str, repo_name: str, work: str = None):
        check = False
        for member_role in interaction.user.roles:
            for _role in roles_list:
                if member_role.name == _role:
                    check = True

        if not check:
            await interaction.response.send_message(f"You don't have permissions", delete_after=3.0)
            return

        response = await message_text(self.client, interaction.channel.name, message_type,
                                      repo_name, work)

        await interaction.response.send_message(response, ephemeral=True, delete_after=3.0)


def setup(client):
    client.add_cog(GenerateMessage(client))
