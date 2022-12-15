import discord
#import datetime

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True

#current_year = datetime.datetime.now().year

class DiscordBot(discord.Client):
    async def on_ready(self):
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
                    continue

                await payload.member.remove_roles(roles)

            if role:
                await payload.member.add_roles(role)

            await reaction.remove(payload.member)

    async def on_member_join(self, member):
        guild = self.get_guild()
        await member.add_roles(discord.utils.get(guild.roles, name='2022'))


client = DiscordBot(intents=intents)

client.run(TOKEN)
