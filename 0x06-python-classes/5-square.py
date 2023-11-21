#!/usr/bin/python3
"""define a class Square"""

class Square:
    """this is a class defined for square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, value):
        if type(self, value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range (self.__size):
            for n in range(self.__size):
                print('#', end="")
            print()
