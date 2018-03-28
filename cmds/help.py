"""
lists all the commands with the prefix as well as their descriptions.
"""


from modules.Command import Command
from master import handler
from master import cfg


name = "help"
group = "standard"
description = "lists all commands and their functions"


@handler.command(Command(name, group, description))
async def list_help(bot, msg, args):
    string = ""
    for key in handler.help:
        string += ("\n`" + cfg["prefix"] + key + " - " + handler.help[key] + "`")
    await bot.send_message(msg.channel, string)
