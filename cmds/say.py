"""
basic command that just repeats the arguments.
mainly used for testing purposes.
"""

from modules.Command import Command
from master import handler


name = "say"
group = "standard"
description = "repeats after you"


@handler.command(Command(name, group, description))
async def say(bot, msg, args):
    await bot.send_message(msg.channel, " ".join(args))