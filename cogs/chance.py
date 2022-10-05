import discord
from discord.ext import commands
import random as r

class Chance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """Flips a coin"""
    @commands.command(pass_context=True)
    async def flipcoin(self, ctx):
        coin = r.randint(0,1)
        if coin == 1:
            coin = "Heads"
        else:
            coin = "Tails"
        await ctx.send("{0}!".format(coin))

    """Rolls an n sided die"""
    @commands.command(pass_context=True)
    async def roll(self, ctx, sides):
        sides = int(sides)
        if sides < 1:
            return
        roll = r.randint(1,sides)
        await ctx.send("Rolled a {0}!".format(roll))

async def setup(bot):
    await bot.add_cog(Chance(bot))