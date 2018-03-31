"""
controls the loading of all files in the cmds directory
"""

import os
import importlib


print("loaded module [loader]")


def load():
    cmdnames = os.listdir("cmds/")
    filtered = []
    for name in cmdnames:
        if name[-3:] == ".py":
            print("loaded command [{}]".format(name[:-3]))
            filtered.append(name)
    for name in filtered:
        m = importlib.import_module("cmds." + name[:-3])
        importlib.reload(m)


async def reload():
    cmdnames = os.listdir("cmds/")
    filtered = []
    for name in cmdnames:
        if name[-3:] == ".py":
            print("loaded command [{}]".format(name[:-3]))
            filtered.append(name)
    for name in filtered:
        m = importlib.import_module("cmds." + name[:-3])
        importlib.reload(m)

