#!/usr/bin/python3
"""
Inheritance
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().integer_validator("width", self.width)
        super().integer_validator("height", self.height)
