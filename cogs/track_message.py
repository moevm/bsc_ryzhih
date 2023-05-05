import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from discord_bot import DiscordBot#, client

roles_list = ['Преподаватель', 'Модератор']

class TrackMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="track_message", description="track_message")
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, message_id: str, roles: str):
        check = False
        for member_role in interaction.user.roles:
            for _role in roles_list:
                if member_role.name == _role:
                    check = True

        if not check:
            await interaction.response.send_message(f"You don't have permissions", ephemeral=True, delete_after=3.0)
            return

        DiscordBot.track_message(self.client, message_id, roles)
        await interaction.response.send_message(f"You track message {message_id} with roles: {roles}", ephemeral=True,
                                        delete_after=3.0)
        return

def setup(client):
    client.add_cog(TrackMessage(client))
