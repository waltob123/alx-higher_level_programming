#!/usr/bin/python3
'''2-post_email.py

a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
'''

import urllib.parse
import urllib.request as req
import sys


if __name__ == '__main__':
    email = sys.argv[2]
    url = sys.argv[1]
    value = {'email': email}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode('utf-8'))
