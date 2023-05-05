# Создание категории
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class AddCategory(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="add_category", description="Add category to the guild", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, category: str):
        await interaction.guild.create_category(name=category)
        await interaction.response.send_message(f"{interaction.user}, u have created category '{category}'",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(AddCategory(client))
