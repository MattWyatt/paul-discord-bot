"""
module responsible for parsing the config as a json object
"""


import json


print("loaded module [config]")


def get():
    with open("config.json", "r") as cfg:
        return json.loads(cfg.read())
