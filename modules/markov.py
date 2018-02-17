"""
module that serves to store markov chains and construct responses with hilarious results.
"""


import sqlite3
from random import randint


def init():
    connection = sqlite3.connect("markov.db")
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS markov (key TEXT, value TEXT)")
    connection.commit()
    connection.close()


def insert(words):
    connection = sqlite3.connect("markov.db")
    c = connection.cursor()
    for iterator in range(0, len(words)):
        key = words[iterator]
        value = ""
        try:
            value = words[iterator+1]
            c.execute("INSERT INTO markov VALUES (?, ?)", (key, value))
        except IndexError:
            continue
    connection.commit()
    c.execute("SELECT * FROM markov")
    connection.close()


def construct_response(words):
    connection = sqlite3.connect("markov.db")
    c = connection.cursor()
    index = randint(0, len(words)-1)
    current = words[index]
    count = 0
    final = ""
    while count < 21:
        count += 1
        c.execute("SELECT value FROM markov WHERE key=?", (current,))
        possible = c.fetchall()
        if len(possible) == 0:
            return final
        current = possible[randint(0, len(possible)-1)][0]
        final += current + " "
    connection.close()
    return final


init()
