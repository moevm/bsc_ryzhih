# Удаление указаной роли у всех участников
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from nextcord.utils import get

class DeleteRole(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="delete_role", description="Delete chosen role from all members", guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, role: str):
        for member in interaction.guild.members:
            await member.remove_roles(get(interaction.guild.roles, name=role))
        await interaction.response.send_message(f"{interaction.user}, u have delete role '{role}' from all members",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(DeleteRole(client))
