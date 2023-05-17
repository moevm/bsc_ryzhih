# Создание категории
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class AddCategory(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664
    groups = ['2300', '2303', '2304', '2381', '2382', '2383', '2384']
    @nextcord.slash_command(name="add_category", description="Add category to the guild", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, name: str, prefix: str):
        category = await interaction.guild.create_category(name=name)
        await interaction.response.send_message(
            f"{interaction.user}, u have created category '{name}' with prefix '{prefix}'",
            ephemeral=True, delete_after=3.0)

        for i in self.groups:
            await interaction.guild.create_text_channel(name=f"{prefix}-{i}", category=category)


def setup(client):
    client.add_cog(AddCategory(client))
