#!/usr/bin/python3
"""
Input/Output
"""
import json


def from_json_string(my_str):
    """
    open file and writes
    """
    return json.loads(my_str)
