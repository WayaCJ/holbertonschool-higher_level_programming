#!/usr/bin/python3
"""
_summary_
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Parent Class Animal"""

    @abstractmethod
    def sound(self):
        """
        Defines the abstract class Animal
        """
        pass


class Dog(Animal):
    """Class Dog"""
    def sound(self):
        """Defines the sound of bark for class Dog"""
        return "Bark"


class Cat(Animal):
    """Class Cat"""
    def sound(self):
        """Defines the sound of Meow for class Cat"""
        return "Meow"
