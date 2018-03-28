"""
grabs a random inspirational image from the inspirobot website.
"""


import discord
import requests
from modules.Command import Command
from master import handler


name = "inspire"
group = "fun"
description = "gets a random inspirational image from http://inspirobot.me"


@handler.command(Command(name, group, description))
async def inspire(bot, msg, args):
    request = requests.get("http://inspirobot.me/api?generate=true")
    if not request.status_code == 200:
        await bot.send_message(msg.channel, "inspirobot failed to generate an inspirational image.")
        return
    embed = discord.Embed(type="rich")
    embed.set_footer(text="retrieved from http://inspirobot.me", icon_url="https://i.imgur.com/Qds5KNu.png")
    embed.set_image(url=request.text)
    await bot.send_message(msg.channel, embed=embed)
