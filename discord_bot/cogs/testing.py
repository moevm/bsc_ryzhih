import nextcord
import os
from nextcord import Interaction
from nextcord.ext import commands, ipc

class Testing(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="testing", guild_ids=[server_id])
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("Testing")

def setup(client):
    client.add_cog(Testing(client))