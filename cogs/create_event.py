#Создание ивента
import nextcord
from nextcord import Interaction
from nextcord.ext import commands, ipc
import enum
import typing

#class Time(enum.Enum):
#    apple = 1
#    banana = 2
#    cherry = 3

class CreateEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="create_event", description="create event", guild_ids=[testServerId])
    @commands.has_permissions(administrator=True)
    async def self(self, interaction: Interaction, title: str, repeat: typing.Literal['week','day'], time: typing.Literal['8', '9'], description: str, roles: str):
        self.client.events.add_event(self.client.events, title, repeat, time, description, roles)
        await interaction.response.send_message(f"U created event", ephemeral=True, delete_after=3.0)

def setup(client):
    client.add_cog(CreateEvent(client))
