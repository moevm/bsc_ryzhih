# Выдача указаной роли всем участникам
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from nextcord.utils import get

class GiveRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="give_role", description="Gives all members the chosen role", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, role: str):
        for member in interaction.guild.members:
            await member.add_roles(get(interaction.guild.roles, name=role))
        await interaction.response.send_message(f"{interaction.user}, u have added role '{role}' to all members",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(GiveRole(client))
