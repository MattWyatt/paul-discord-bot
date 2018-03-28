"""
this module is simply the Handler class, built to handle commands as events.
commands are registered by storing the names and functions, respectively, in a dictionary.
commands are called by their name ( ex: commands["say"](arguments) )
"""


class Handler:
    def __init__(self, bot):
        self.commands = {}
        self.help = {}
        self.bot = bot

    def set(self, bot):
        self.bot = bot

    def has(self, cmdname):
        if cmdname in self.commands:
            return True
        return False

    async def call(self, cmdname, cmdmsg, cmdargs):
        if cmdname in self.commands:
            await self.commands[cmdname](self.bot, cmdmsg, cmdargs)
        else:
            print("no command found")

    def command(self, command_object):
        def registrar(func):
            cmdname = command_object.name
            desc = command_object.description
            self.commands[cmdname] = func
            self.help[cmdname] = desc
        return registrar
