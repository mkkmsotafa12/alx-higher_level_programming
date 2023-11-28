#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """define a class's attributes,
    which reduces memory usage and prevents dynamic attributes
    from being created."""
    __slots__ = ['first_name']
