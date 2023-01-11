# Тест работы команд
import discord
from discord.ext import commands
from discord import app_commands

from discord_bot import tree


@tree.command(name="test", description="test", guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}")


# Очистка сообщений канала
@tree.command(name="clear", description="Clear chosen amount of chat messages",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.response.send_message(f"{ctx.user}, u have deleted {len(deleted)} messages", ephemeral=True)


# Выдача указаной роли всем участникам
@tree.command(name="give_role", description="Gives all members the chosen role",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    for member in ctx.guild.members:
        await member.add_roles(discord.utils.get(ctx.guild.roles, name=role))
    await ctx.response.send_message(f"{ctx.user}, u have added role '{role}' to all members", ephemeral=True)


# Удаление указаной роли у всех участников
@tree.command(name="delete_role", description="Delete chosen role from all members",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    for member in ctx.guild.members:
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name=role))
    await ctx.response.send_message(f"{ctx.user}, u have delete role '{role}' from all members", ephemeral=True)


# Создание категории
@tree.command(name="add_category", description="Add category to the guild",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, category: str):
    await ctx.guild.create_category(name=category)
    await ctx.response.send_message(f"{ctx.user}, u have created category '{category}'", ephemeral=True)


# Удаление пользователей указаной роли
@tree.command(name="delete_members_by_role", description="Delete all members attached to chosen role",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, role: str):
    members = []
    for member in ctx.guild.members:
        if discord.utils.get(ctx.guild.roles, name=role) in member.roles:
            members.append(await member.kick())
    await ctx.response.send_message(f"{ctx.user}, u have kicked '{len(members)}' members", ephemeral=True)