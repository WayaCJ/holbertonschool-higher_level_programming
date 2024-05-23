#!/usr/bin/python3
""" function that lookup attributes and methods of an object"""


def lookup(obj):
    """function to return the list of available attributes
     and methods of an obj
     """
    return dir(obj)
