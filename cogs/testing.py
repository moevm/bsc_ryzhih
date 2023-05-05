import nextcord
import os
from nextcord import Interaction
from nextcord.ext import commands, ipc

class Testing(commands.Cog):
    def __init__(self, my_bot):
        self.my_bot = my_bot

    testServerId = 1001473537451761664

    @nextcord.slash_command(name="testing", guild_ids=[testServerId])
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("Testing")

def setup(my_bot):
    my_bot.add_cog(Testing(my_bot))