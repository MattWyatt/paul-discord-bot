import discord
from random import randint


print("loaded module [fools]")


async def super_everyone(bot, channel):
    member_array = []
    for member in channel.server.members:
        member_array.append(member)

    num_members = len(member_array)
    iterator_start = 0
    for num in range(0, round(num_members / 10)):
        mention_str = ""
        for index in range(0, 10):
            try:
                mention_str += member_array[index+iterator_start].mention
                mention_str += " "
            except IndexError:
                break

        iterator_start += 10
        await bot.send_message(channel, mention_str)


async def someone(bot, channel):
    member_array = []
    for member in channel.server.members:
        member_array.append(member)
    x = randint(0, len(member_array))
    await bot.send_message(channel, member_array[x].mention)


async def cry_of_despair(bot, member):
    if member.voice_channel:
        if not bot.voice_client_in(member.server):
            await bot.join_voice_channel(member.voice_channel)
        cry = bot.voice_client_in(member.server).create_ffmpeg_player("res/cry_of_despair.m4a")
        cry.start()
