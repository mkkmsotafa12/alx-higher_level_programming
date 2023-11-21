#!/usr/bin/python3
"""writing an empty class"""

class Square:
    """this is a class defined for square.

    Args:
        size (int): length of one side of square
        position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines


    Attributes:
        __size (int): length of one side of square
        __position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines"""


    def __init__(self, size=0, position=(0, 0)):
        # attribute assigment here engages setters defined below
        self.__size = size
        self.potition = size


    @property
    def size(self):
        """size getter, setter with same method name

            Returns:
                size (int): the length of one side, squared

            """
        return self.__size


    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.potition

    @position.setter
    def position(self, value):
        """Args:
            value (int): tuple of two positive integers

                Attributes:
                     __position (tuple) ((int), (int)): horizontal offset in spaces,
                    vertical offset in newlines

                Raises:
                     TypeError: if value is not a tuple of two positive ints"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for n in value:
            if type(n) != int or n < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.potition = value
    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
            """Prints text representation of square in hash chars,
            horizontally and vertically offset by first and second int
            in __position, respectively.

            Attributes:
                 __size (int): length of one side of square
                 __position (tuple) ((int), (int)): horizontal offset in spaces,
                vertical offset in newlines"""


            if self.__size == 0:
                print()
            else:
                for v_offset in range(0, self.__position[1]):
                     print()
                for row in range(0, self.__size):
                    for h_offset in range(0, self.__position[0]):
                        print(" ", end="")
                    for col in range(0, self.__size):
                        print("#", end="")
                    print()

    #   print("size: {} position: {}".format(self.__size, self.__position))
