"""
just grabs a random dog picture from random.dog.
cats are better.
"""


import discord
import requests
from master import handler
description = "grabs a random dog from https://random.dog"


@handler.command("dog", description)
async def dog(bot, msg, args):
    request = requests.get("https://random.dog/woof")
    if not request.status_code == 200:
        await bot.send_message(msg.channel, "the site failed to retrieve a random dog.")
        return
    embed = None
    if ".mp4" in request.text:
        embed = discord.Embed(video=request.text, type="rich")
        embed.set_footer(text="retrieved from https://random.dog", icon_url="https://i.imgur.com/riA2zNy.jpg")
        embed.set_image(url="https://random.dog/" + request.text)
        return
    else:
        embed = discord.Embed(type="rich")
        embed.set_footer(text="retrieved from https://random.dog", icon_url="https://i.imgur.com/riA2zNy.jpg")
        embed.set_image(url="https://random.dog/" + request.text)
    await bot.send_message(msg.channel, embed=embed)