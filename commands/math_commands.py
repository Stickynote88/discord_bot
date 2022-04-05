import discord
from discord.ext import commands
class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    """Adds the numbers given"""
    @commands.command(pass_context=True)
    async def add(self, ctx, *args):
        total = 0
        for arg in args:
            total +=int(arg)
        await ctx.send("That equals {0}!".format(total))

def setup(bot):
    bot.add_cog(Math(bot))