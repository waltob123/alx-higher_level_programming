#!/usr/bin/python3
'''1-hbtn_header.py

a Python script that takes in a URL, sends a
request to the URL and displays the value of
the X-Request-Id variable found in the header
of the response.
'''


import sys
import urllib.request as req


if __name__ == '__main__':
    url = sys.argv[1]
    request = req.Request(url)
    with req.urlopen(request) as response:
        print(response.headers.get('X-Request-Id'))
