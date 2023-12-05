#!/usr/bin/python3
"""
Input/Output
"""


def write_file(filename="", text=""):
    """
    open file and writes
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
