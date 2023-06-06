# Очистка сообщений канала
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class Clear(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="clear", description="Clear chosen amount of chat messages", guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"{interaction.user}, u have deleted {len(deleted)} messages",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(Clear(client))
