"""
command for playing youtube urls in voice chat
"""

from modules.Command import Command
from master import handler
import requests


name = "play"
group = "fun"
description = "plays a supplied youtube url"


@handler.command(Command(name, group, description))
async def play(bot, msg, args):
    if not msg.author.voice_channel:
        await bot.send_message(msg.channel, "you need to be in a voice channel to use this command")
        return
    if not len(args) > 0:
        await bot.send_message(msg.channel, "no url supplied")
        return
    try:
        requests.head(args[0])
    except:
        await bot.send_message(msg.channel, "invalid url supplied")
        return

    if not bot.voice_client_in(msg.author.server):
        await bot.join_voice_channel(msg.author.voice_channel)
    yt_player = await bot.voice_client_in(msg.author.server).create_ytdl_player(args[0])
    await bot.send_message(msg.channel, "playing `{}`!".format(yt_player.title))
    yt_player.start()
