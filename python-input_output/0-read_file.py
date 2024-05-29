#!/usr/bin/python3
"""Module that creates def read_file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
