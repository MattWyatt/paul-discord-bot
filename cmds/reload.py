"""
reloads all commands
"""

from modules.loader import load
from modules.Command import Command
from master import handler


name = "reload"
group = "admin"
description = "reloads all commands"


@handler.command(Command(name, group, description))
async def say(bot, msg, args):
    load()
    await bot.send_message(msg.channel, "reloaded all commands!")
