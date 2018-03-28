"""
this command grabs a random cat picture from random.cat.
it's my favorite command.
"""


import discord
import requests
from modules.Command import Command
from master import handler


name = "cat"
group = "fun"
description = "grabs a random cat from https://aws.random.cat"


@handler.command(Command(name, group, description))
async def cat(bot, msg, args):
    request = requests.get("https://aws.random.cat/meow")
    if not request.status_code == 200:
        await bot.send_message(msg.channel, "the site failed to retrieve a random cat.")
        return
    embed = discord.Embed(type="rich")
    embed.set_footer(text="retrieved from https://aws.random.cat", icon_url="https://i.imgur.com/ubfAGCI.png")
    embed.set_image(url=request.json()["file"])
    await bot.send_message(msg.channel, embed=embed)