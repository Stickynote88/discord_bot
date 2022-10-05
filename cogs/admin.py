import discord
from discord.ext import commands
from discord.ext.commands import has_role

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.is_owner()
    @has_role("Caretaker")
    async def change_status(self, ctx, *args):
        await commands.change_presence(activity=discord.Game(name=" ".join(args)))

    @change_status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You don't possess the role for that bucko ")

async def setup(bot):
    await bot.add_cog(Admin(bot))