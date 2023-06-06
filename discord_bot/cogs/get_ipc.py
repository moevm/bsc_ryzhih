# Очистка сообщений канала
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class GetIPC(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="get_ipc", guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction):
        await interaction.response.send_message(f"{self.client.ipc.endpoints};",
                                                ephemeral=True)

def setup(client):
    client.add_cog(GetIPC(client))
