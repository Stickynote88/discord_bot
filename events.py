import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

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

