#!/usr/bin/python3
"""Inheritance"""


def inherits_from(obj, a_class):
    """Returns true if the object is an instance of a class that
    inherits from a specified class, directly or indirectly, else
    false"""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return (True)
    return (False)
