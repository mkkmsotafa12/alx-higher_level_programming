#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to the URL """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as f:
        headers = f.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
                break