import discord
from discord.ext import commands
from discord import app_commands

# import datetime

TOKEN = 'MTA1MDU2Mzk5NzM2OTM3MjcyMw.GlG_3e.jGFZ04VU9eGLUuMifzPjieaHGIyxGLbGVyabLI'

intents = discord.Intents.all()
intents.message_content = True


# current_year = datetime.datetime.now().year

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
        if message.author == client.user:
            return

        if message.content.lower() == 'hello':
            await message.channel.send(f'Hello, {message.author.display_name}!')

            return

        if message.content.lower() == 'bye':
            await message.channel.send(f'See you later, {message.author.display_name}!')

            return

    async def on_raw_reaction_add(self, payload):
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = client.get_guild(payload.guild_id)
        reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
        print(reaction)

        if payload.member.id == client.user.id:
            return

        if payload.message_id == 1053040934671101983:
            print(payload.member.roles)
            match reaction.emoji:
                case '🟥':
                    role = discord.utils.get(guild.roles, name='role1')
                case '🟨':
                    role = discord.utils.get(guild.roles, name='role2')
                case '🟦':
                    role = discord.utils.get(guild.roles, name='role3')
                case _:
                    role = None

            for roles in payload.member.roles:
                if roles == discord.utils.get(guild.roles, name='@everyone'):
                    print(roles)
                    continue
                print(roles)
                await payload.member.remove_roles(roles)

            if role:
                await payload.member.add_roles(role)

            await reaction.remove(payload.member)

    async def on_member_join(self, member):
        guild = self.get_guild(1031609704188739614)
        await member.add_roles(discord.utils.get(guild.roles, name='2022'))


client = DiscordBot()
tree = app_commands.CommandTree(client)

#Тест работы команд
@tree.command(name="test", description="test", guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}")

#Очистка сообщений канала
@tree.command(name="clear", description="Clear chosen amount of chat messages",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.response.send_message(f"{ctx.user}, u have deleted {len(deleted)} messages", ephemeral=True)

#Выдача указаной роли всем участникам
@tree.command(name="give_role", description="Gives all members the chosen role",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    for member in ctx.guild.members:
        await member.add_roles(discord.utils.get(ctx.guild.roles, name=role))
    await ctx.response.send_message(f"{ctx.user}, u have added role '{role}' to all members", ephemeral=True)

#Удаление указаной роли у всех участников
@tree.command(name="delete_role", description="Delete chosen role from all members",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    for member in ctx.guild.members:
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name=role))
    await ctx.response.send_message(f"{ctx.user}, u have delete role '{role}' from all members", ephemeral=True)

#Создание категории
@tree.command(name="add_category", description="Add category to the guild",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, category: str):
    await ctx.guild.create_category(name=category)
    await ctx.response.send_message(f"{ctx.user}, u have created category '{category}'", ephemeral=True)

#Удаление пользователей указаной роли
@tree.command(name="delete_members_by_role", description="Delete all members attached to chosen role",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    members = []
    for member in ctx.guild.members:
        if discord.utils.get(ctx.guild.roles, name=role) in member.roles:
            members.append(await member.kick())
    await ctx.response.send_message(f"{ctx.user}, u have kicked '{len(members)}' members", ephemeral=True)

client.run(TOKEN)
