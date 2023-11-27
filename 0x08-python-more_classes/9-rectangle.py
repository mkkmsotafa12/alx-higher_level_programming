#!/usr/bin/python3

"""
more classes and objects in python
"""


class Rectangle:
    """
    the class Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__
            Arg:
            width : width of rectangle
            height : height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """"width of the getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This is height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area by method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter by method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """__repr__ """
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """__str__ """
        if self.__width == 0 or self.__height == 0:
            return ""
        str__ = ""
        return '\n'.join([str(self.prit_sym) * self.__width] *
                         self.__height)

    def __del__(self):
        """__del__ """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
