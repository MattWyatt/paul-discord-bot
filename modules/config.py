"""
module responsible for parsing the config as a json object
"""


import json


def get():
    with open("config.json", "r") as cfg:
        return json.loads(cfg.read())
