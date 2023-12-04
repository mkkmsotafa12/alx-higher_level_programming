#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class My_list:
    """the class of my_list inherits from list"""

    def print_sorted(self):
        """Public instance method"""
        list_sorted = sorted(self)
        print(list_sorted)
