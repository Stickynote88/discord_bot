import discord
from discord.ext import commands
import random as r

class Chance(commands.Cog):
    import random as r

    def __init__(self, bot):
        self.bot = bot

    """Flips a coin"""
    @commands.command()
    async def flipcoin(ctx):
        coin = r.randint(0,1)
        if coin == 1:
            coin = "Heads"
        else:
            coin = "Tails"
        await ctx.send("{0}!".format(coin))

    """Rolls a n sided die"""
    @commands.command()
    async def roll(ctx, sides):
        sides = int(sides)
        if sides < 1:
            return
        roll = r.randint(1,sides)
        await ctx.send("Rolled a {0}!".format(roll))

class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """Returns greeting"""
    @commands.command()
    async def hello(ctx):
        await ctx.send("Hello!")

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    """Adds the numbers given"""
    @commands.command()
    async def add(ctx, *args):
        total = 0
        for arg in args:
            total +=int(arg)
        await ctx.send("That equals {0}!".format(total))

def setup(bot):
    bot.add_cog(Chance(bot))
    bot.add_cog(Chat(bot))
    bot.add_cog(Math(bot))