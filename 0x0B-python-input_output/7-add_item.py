#!/usr/bin/python3
"""
Input/Output
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    read = load_from_json_file('add_item.json')
except FileNotFoundError:
    read = []
read.extend(sys.argv[1:])
save_to_json_file(read, 'add_item.json')
