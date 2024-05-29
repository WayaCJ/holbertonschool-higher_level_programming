#!/usr/bin/python3
"""Module for the function that appends a string
at the end of a text file and returns the number
 of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
