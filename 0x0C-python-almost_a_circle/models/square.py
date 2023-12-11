#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        """initalization to size of square"""
        self.width = value
        self.height = value

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updating the public method"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of this class"""
        return {"size": self.width, "y": self.y,
                "x": self.x, "id": self.id}
