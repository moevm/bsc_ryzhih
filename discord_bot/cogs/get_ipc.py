# Очистка сообщений канала
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class GetIPC(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="get_ipc", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction):
        await interaction.response.send_message(f"{self.client.ipc.endpoints};",
                                                ephemeral=True)

def setup(client):
    client.add_cog(GetIPC(client))
