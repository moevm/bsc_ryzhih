# Получение списка пул-реквестов
import re
import discord
from discord.utils import get
from discord.ext import commands
from transliterate import translit
from discord_bot import tree, DiscordBot, generate_message, get_pulls


@tree.command(name="generate_message", description="Generate message for students")#,guild=discord.Object(id=1031609704188739614))
@commands.has_permissions(administrator=True)
async def self(ctx: commands.Context, message_type: str, role: discord.Role, work: str = None):
    text = await generate_message(message_type)
    text_begin, text_end = text.split('$people')
    pulls = await get_pulls()
    mentions = ""
    work_number = None
    for pr in pulls:
        surname, name, work_type = re.findall('[^_]+', pr.title)

        if work_type != work and work is not None:
            continue

        group = re.search('\d+', ctx.channel.name)
        if group is None:
            await ctx.response.send_message("Вы не в канале группы!", ephemeral=True, delete_after=3.0)
            return

        full_nick = surname + '.' + name + '.' + group[0]

        nick = full_nick.replace('ya', 'ja')
        nick = translit(nick, 'ru')
        user = get(ctx.guild.members, nick=nick)

        if work:
            work_number = re.search('\d+', work)[0]
        if work_number:
            mentions += '\n' + user.mention + f" -- Лабораторная работа номер {work_number}"
        elif work_number == 'cw':
            mentions += '\n' + user.mention + f" -- Курсовая работа"
        else:
            mentions += '\n' + user.mention + f" -- работа {work_type}"

    await ctx.channel.send(f"""
        {role.mention}
        {text_begin}
        {mentions}
        {text_end}
        """)
    await ctx.response.send_message("Success!", ephemeral=True, delete_after=3.0)
