#!/usr/bin/python3
""" Displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    ur = sys.argv[1]

    r = requests.get(ur)
    print(r.headers.get("X-Request-Id"))