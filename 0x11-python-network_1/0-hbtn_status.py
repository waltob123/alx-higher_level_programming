#!/usr/bin/python3
'''hbtn_status.py

a Python script that fetches https://alx-intranet.hbtn.io/status
'''


import urllib.request as req


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    request = req.Request(url)
    with req.urlopen(request) as response:
        body = response.read()
        print('Body response:$')
        print(f'\t- type: {type(body)}$')
        print(f'\t- content: {body}$')
        print(f'\t- utf8 content: {body.decode("utf-8")}$')
