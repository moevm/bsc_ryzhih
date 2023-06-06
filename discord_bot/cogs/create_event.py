#Создание ивента
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
import enum
import typing

class CreateEvent(commands.Cog):
    server_id = None

    def __init__(self, client):
        self.client = client
        self.server_id = client.server_id

    @nextcord.slash_command(name="create_event", description="create event", guild_ids=[server_id])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, title: str, repeat: typing.Literal['no', 'day', 'week', '2 weeks'],
                   time: str, data: str, description: str, roles: str):
        self.client.events.add_event(self.client.events, title, repeat, time, data, description, roles)
        await interaction.response.send_message(f"U created event", ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(CreateEvent(client))
