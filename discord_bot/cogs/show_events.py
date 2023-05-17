#Вывод ивентов
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc

class ShowEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="show_events", description="show events", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction):
        msgs = self.client.events.show(self.client.events)
        for msg in msgs:
            await interaction.channel.send(embed=msg)

def setup(client):
    client.add_cog(ShowEvents(client))
