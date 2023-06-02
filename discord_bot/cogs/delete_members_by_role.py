# Удаление пользователей указаной роли
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
from nextcord.utils import get

class DeleteMembersByRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="delete_members_by_role", description="Delete all members attached to chosen role", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, role: str):
        members = []
        for member in interaction.guild.members:
            if get(interaction.guild.roles, name=role) in member.roles:
                members.append(await member.kick())
        await interaction.response.send_message(f"{interaction.user}, u have kicked '{len(members)}' members",
                                                ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(DeleteMembersByRole(client))
