"""
basic command that just repeats the arguments.
mainly used for testing purposes.
"""

from master import handler
description = "repeats after you"


@handler.command("say", description)
async def say(bot, msg, args):
    await bot.send_message(msg.channel, " ".join(args))
