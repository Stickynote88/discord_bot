import commands
import json

tokens = json.load(open(file="./tokens.json", encoding="utf-8"))

bot = commands()

bot.run(tokens["token"])