import discord, json, asyncio, os
from discord.ext import commands


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

# Events

"""On Ready: Prints to terminal when bot is ready, states bots id"""
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

"""On Message: This is where the smirking magic happens, smirks any post made in meme chat"""
@bot.event
async def on_message(message):
    # Whenever a post is made in selected channel, reacts with smirk
    if str((message.channel)) == "memes😏":
        await message.add_reaction("😏")
        print("Message from {0.author.name} in {0.guild.name} getting smirked 😏 \nMessage contents : {0.content}"
            .format(message))

    await bot.process_commands(message)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f"Loading {filename[:-3]} cog...", end =" ")
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Done")

async def main():
    async with bot:

        await load_extensions()
        tokens = json.load(open(file="./tokens.json", encoding="utf-8"))
        await bot.start(tokens["token"])

asyncio.run(main())