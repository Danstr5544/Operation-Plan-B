from redbot.core import commands

class dmmail(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dmmail(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Wrong bot - DM <@1126941023159992440>. Use the **__?__** Prefix rather than the usual ! Prefix")
