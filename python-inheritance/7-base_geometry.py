#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Method Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if int != type(value):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
