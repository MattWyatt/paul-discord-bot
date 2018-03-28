"""
this module handles anything used throughout the whole bot.
it includes references to the global client instance, the global handler instance, and pre-loads the cfg.
"""

import discord
from modules import config
from modules.Handler import Handler
cfg = config.get()
client = discord.Client()
handler = Handler(client)