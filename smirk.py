import discord
import json

tokens = json.load(open(file="./tokens.json", encoding="utf-8"))
config = json.load(open(file="./config.json", encoding="utf-8"))

game = discord.Game(config["game"])
client = discord.Client(status=discord.Status.online, activity=game)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    print("On message called")
    # If message came from bot, ignore it and return
    if message.author == client.user:
        print("Bot message, ignoring")
        return
    # If message starts with "$hello", bot responds
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
        print("Sending Hello")
    
    # Whenever a post is made in selected channel, reacts with smirk
    if str((message.channel)) == config["smirking_channel"]:
        await message.add_reaction("😏")
        print("Smirking post in {channel}".format(channel = config["smirking_channel"]))


client.run(tokens["token"])






