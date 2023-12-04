#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """the class of my_list inherits from list"""

    def print_sorted(self):
        """Public instance method"""
        sorted_list = sorted(self)
        print(sorted_list)
