import discord

class DiscordManager:
    async def send_message(message, user):
        if message.author == user:
            return

        if message.content.lower() == 'hello':
            await message.channel.send(f'Hello, {message.author.display_name}!')

            return

        if message.content.lower() == 'bye':
            await message.channel.send(f'See you later, {message.author.display_name}!')

            return

    async def add_role_by_reaction(client, payload, message_id):
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = client.get_guild(payload.guild_id)
        reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)

        if payload.member.id == client.user.id:
            return

        if payload.message_id == message_id:
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