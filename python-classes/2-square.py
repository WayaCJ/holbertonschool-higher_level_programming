#!/usr/bin/python3
"""This module defines a class called Square
    Raises:
        size must be an integer, otherwise raise a TypeError
        size must be greater than 0, otherwise raise a ValueError
"""

class Square:
    """class Square
    """
    def __init__(self, size=0):
        """
        Args:
        size: Private instance attribute defaults to zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
