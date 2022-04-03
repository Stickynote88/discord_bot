import discord
import json

tokens = json.load(open(file="./tokens.json", encoding="utf-8"))

game = discord.Game("Five Nights at Freddy's")
client = discord.Client(status=discord.Status.online, activity=game)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    print("On message called")
    # If message came from client, ignore it and return
    if message.author == client.user:
        print("client message, ignoring")
        return
    # If message starts with "$hello", client responds
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
        print("Sending Hello")
    
    # Whenever a post is made in selected channel, reacts with smirk
    if str((message.channel)) == "memes😏":
        await message.add_reaction("😏")
        print("Message from {0.author.name} in {0.guild.name} getting smirked 😏 \nMessage contents : {0.content}"
            .format(message))



client.run(tokens["token"])






