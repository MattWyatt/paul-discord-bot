"""
this module is responsible for parsing out the various sections of messages.
"""


from master import cfg


print("loaded module [parser]")

def parse_command(content):
    string = content[len(cfg["prefix"]):]
    string = string.split(" ")
    return string[0]


def parse_args(content):
    string = content[len(cfg["prefix"]):]
    string = string.split(" ")
    return string[1:]


def parse_markov(content):
    string = content[len(cfg["markov_prefix"])+1:]
    string = string.split(" ")
    return string
