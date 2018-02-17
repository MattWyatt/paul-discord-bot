"""
lists all the commands with the prefix as well as their descriptions.
"""


from master import handler
from master import cfg
description = "lists all commands and their functions"


@handler.command("help", description)
async def list_help(bot, msg, args):
    string = ""
    for key in handler.help:
        string += ("\n`" + cfg["prefix"] + key + " - " + handler.help[key] + "`")
    await bot.send_message(msg.channel, string)
