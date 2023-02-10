import discord
from discord.ext import commands

from discord_bot import tree, DiscordBot, client


@tree.command(name="track_message", description="track_message")#, guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, message_id: str, roles: str):
    DiscordBot.track_message(client, message_id, roles)
    print(roles.split(','))
