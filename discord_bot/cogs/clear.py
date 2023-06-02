# Очистка сообщений канала
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="clear", description="Clear chosen amount of chat messages", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"{interaction.user}, u have deleted {len(deleted)} messages",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(Clear(client))
