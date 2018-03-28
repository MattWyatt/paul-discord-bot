import os
import glob
import importlib


def load():
    cmdnames = os.listdir("cmds/")
    filtered = []
    for name in cmdnames:
        if name[-3:] == ".py":
            print("added", name)
            filtered.append(name)
    for name in filtered:
        print(filtered)
        m = importlib.import_module("cmds." + name[:-3])
        importlib.reload(m)

