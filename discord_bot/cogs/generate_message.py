# Получение списка пул-реквестов
import re
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from nextcord.utils import get
from discord_bot import generate_message, get_pulls

#async def generate_message(message_type):
#    with open('settings.json', 'r', encoding='utf_8_sig') as f:
#        settings = json.load(f)
#    return settings["messages"][message_type]

#async def get_pulls(repo_name):
#    repo = git.get_repo(repo_name)
#    pulls = repo.get_pulls(state='open', sort='created')
#    return pulls

roles_list = ['Преподаватель', 'Модератор']

class GenerateMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="generate_message", description="Generate message for students", guild_ids=[testServerId])
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

        text = await generate_message(message_type)
        text_begin, text_end = text.split('$people')
        pulls = await get_pulls(repo_name)
        mentions = ""
        work_number = None
        for pr in pulls:
            try:
                surname, name, work_type = re.findall('[^_]+', pr.title)
            except:
                await interaction.channel.send(f"""
                            {text_begin}
                            {pr.title}
                            {text_end}
                            """)
                await interaction.response.send_message("Success!", ephemeral=True, delete_after=3.0)
                return

            if work_type != work and work is not None:
                continue

            group = re.search('\d+', interaction.channel.name)
            if group is None:
                await interaction.response.send_message("You are not in the channel group!", ephemeral=True, delete_after=3.0)
                return

            full_nick = surname + '.' + name + '.' + group[0]
            nick = full_nick.replace('ya', 'ja')
            # nick = translit(nick, 'ru')
            user = get(interaction.guild.members, nick=nick)

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

        if len(mentions) == 0:
            await interaction.response.send_message("No one has done this job", ephemeral=True, delete_after=3.0)
            return

        await interaction.channel.send(f"""
                {text_begin}
                {mentions}
                {text_end}
                """)
        await interaction.response.send_message("Success!", ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(GenerateMessage(client))
