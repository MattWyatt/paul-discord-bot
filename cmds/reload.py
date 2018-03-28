"""
reloads all commands
"""


import modules.loader
from modules.Command import Command
from master import handler


name = "reload"
group = "admin"
description = "reloads all commands"


@handler.command(Command(name, group, description))
async def reload(bot, msg, args):
    await modules.loader.reload()
    await bot.send_message(msg.channel, "reloaded all commands!")
