#!/usr/bin/python3
"""
Input/Output
"""


def append_write(filename="", text=""):
    """
    open file and writes
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
