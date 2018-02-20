"""
this is the main application master.
this master is responsible for listening for client events and running commands.
"""

from modules import parser
from modules import markov
from master import cfg
from master import client
from master import handler
from cmds import *


@client.event
async def on_ready():
    print("logged in as [" + client.user.name + "]")
    print("with id [" + client.user.id + "]")


@client.event
async def on_message(message):
    markov.insert(message.content.split(" "))
    if message.content.startswith(cfg["prefix"]):
        cmd = parser.parse_command(message.content)
        args = parser.parse_args(message.content)
        if handler.has(cmd):
            await handler.call(cmd, message, args)
        else:
            await client.send_message(message.channel, "invalid command `" + cmd + "`")
    elif message.content.startswith(cfg["markov_prefix"]+" "):
        response = await markov.construct_response(parser.parse_markov(message.content))
        await client.send_message(message.channel, response)


client.run(cfg["token"])
