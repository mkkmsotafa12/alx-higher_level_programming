#!/usr/bin/python3
""" A python script sends a POST request to the passed URL
    with the email as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    ur = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    res = requests.post(ur, data=data)
    print(res.text)
