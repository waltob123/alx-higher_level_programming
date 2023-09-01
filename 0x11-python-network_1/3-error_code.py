#!/usr/bin/python3
"""3-error_code.py

sends a request to a given URL and displays
the response body.
"""


import sys
import urllib.error
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
