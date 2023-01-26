# Получение списка пул-реквестов
import discord
from discord.ext import commands

from discord_bot import tree, DiscordBot


@tree.command(name="generate_message", description="Generate message for students",
              guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, message_type: str):
    text = await DiscordBot.generate_message(message_type)
    await ctx.response.send_message(text, ephemeral=False)