#!/usr/bin/python3
""" this is writing a class"""


class Square:
    """this is a class defined for square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
