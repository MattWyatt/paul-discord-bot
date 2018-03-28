"""
just links to the source of the bot
"""

import discord
from modules.Command import Command
from master import handler


name = "source"
group = "standard"
description = "links to the source for the bot. you can report bugs on the 'issues' page"


@handler.command(Command(name, group, description))
async def source(bot, msg, args):
    embed = discord.Embed(title="paul-discord-bot",
                          url="https://github.com/MattWyatt/paul-discord-bot",
                          description="just a bot named paul and written in python. report bugs here.",
                          type="rich")
    embed.set_thumbnail(url="https://i.imgur.com/rMONFMC.png")
    await bot.send_message(msg.channel, embed=embed)
