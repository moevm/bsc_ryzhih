#Вывод ивентов
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class ShowEvents(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="show_events", description="show events", guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction):
        msgs = self.client.events.show(self.client.events)
        for msg in msgs:
            await interaction.channel.send(embed=msg)

def setup(client):
    client.add_cog(ShowEvents(client))
