import discord
from discord.ext import commands
import functools
from discord_bot import tree, DiscordBot, client

roles_list = ['Преподаватель', 'Модератор']

@tree.command(name="track_message", description="track_message")#, guild=discord.Object(id=1031609704188739614))
async def self(interaction: discord.Interaction, message_id: str, roles: str):
    check = False
    for member_role in interaction.user.roles:
        for _role in roles_list:
            if member_role.name == _role:
                check = True

    if not check:
        await interaction.response.send_message(f"You don't have permissions", delete_after=3.0)
        return

    DiscordBot.track_message(client, message_id, roles)
    await interaction.response.send_message(f"You track message {message_id} with roles: {roles}",
                                                        delete_after=3.0)
    return