#!/usr/bin/python3
"""function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """function to write a string to text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
