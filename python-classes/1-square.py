#!/usr/bin/python3
"""This module defines a class called Square"""


class Square:
    """Class Square
        
        Attributes:
        Private instance attribute: size

        """
    def __init__(self, size):
        """Args:
        size: no type/value verification
        """
        self.__size = size
    def size(self):
        return self.__size
    def set_size(self, value):
        self.__size = value
