import discord
from discord.ext import commands

class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """Returns greeting"""
    @commands.command(pass_context=True)
    async def hello(self, ctx):
        await ctx.send("Hello {0.author.name}!".format(ctx))

async def setup(bot):
    await bot.add_cog(Chat(bot))