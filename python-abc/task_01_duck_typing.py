#!/usr/bin/python3
"""Imports for the module"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """class Shape"""
    @abstractmethod
    def area(self):
        """Defines the area of the class Shape"""
        pass

    def perimeter(self):
        """Defines the perimeter of the class Shape"""
        pass


class Circle(Shape):
    """class Circle with parent class Shape"""
    def __init__(self, radius):
        """Initialized the radius"""
        self.radius = radius

    def area(self):
        """defines the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """defines the perimeter of the circle"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """class Rectangle with parent class Shape"""
    def __init__(self, width, height):
        """initializes the width and height"""
        self.width = width
        self.height = height

    def area(self):
        """defines the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """defines the area of the perimeter"""
        return (self.width + self.height) * 2


def shape_info(shape):
    """defines the shape information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
