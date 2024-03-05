#!/usr/bin/python3
"""A script that send req and display body
"""
import sys
import requests


if __name__ == "__main__":
    ur = sys.argv[1]

    r = requests.get(ur)
    fixed_num = 400
    if r.status_code >= fixed_num:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)