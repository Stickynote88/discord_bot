import discord
from discord.ext import commands
import json
import random as r

tokens = json.load(open(file="./tokens.json", encoding="utf-8"))
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

# Events

"""On Ready: Prints to terminal when bot is ready, states bots id"""
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

"""On Message: This is where the smirking magic happens, smirks any post made in meme chat"""
@bot.event
async def on_message(message):
    # If message came from client, ignore it and return
    if message.author == bot.user:
        print("bot message, ignoring")
        return

    # Whenever a post is made in selected channel, reacts with smirk
    if str((message.channel)) == "memes😏":
        await message.add_reaction("😏")
        print("Message from {0.author.name} in {0.guild.name} getting smirked 😏 \nMessage contents : {0.content}"
            .format(message))
    await bot.process_commands(message)


# Commands

"""Returns greeting"""
@bot.command()
async def hello(ctx):
    print("Inside")
    await ctx.send("Hello!")

"""Adds the numbers given"""
@bot.command()
async def add(ctx, *args):
    total = 0
    for arg in args:
        total +=int(arg)
    await ctx.send("That equals {0}!".format(total))

"""Flips a coin"""
@bot.command()
async def flipcoin(ctx):
    coin = r.randint(0,1)
    if coin == 1:
        coin = "Heads"
    else:
        coin = "Tails"
    await ctx.send("{0}!".format(coin))

"""Rolls a n sided die"""
@bot.command()
async def roll(ctx, sides):
    sides = int(sides)
    if sides < 1:
        return
    roll = r.randint(1,sides)
    await ctx.send("Rolled a {0}!".format(roll))

bot.run(tokens["token"])

