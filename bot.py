import discord
from discord.ext import commands
import json

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


cogs = ["commands"]

for cog in cogs:
    bot.load_extension(cog)
    print("Loaded {0}".format(cog))

bot.run(tokens["token"])

