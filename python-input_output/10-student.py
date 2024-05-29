#!/usr/bin/python3
"""Module class Student"""


class Student:
    """Class student dictionary"""
    def __init__(self, first_name, last_name, age):
        """Instantance with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            attrs = self.__dict__.keys()

        serializable_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                serializable_dict[attr] = getattr(self, attr)
        return serializable_dict
