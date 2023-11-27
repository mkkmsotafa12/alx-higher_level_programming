#!/usr/bin/python3
"""Module for print_square method."""



def print_square(size):
    """
    Write a function that prints a square with the character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            elem = []
            for i in range(size):
                elem.append('#')
            print("".join(elem))
