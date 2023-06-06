import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from discord_bot import DiscordBot#, client

roles_list = ['Преподаватель', 'Модератор']

class TrackMessage(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="track_message", description="track_message", guild_ids=[server_id])
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
