#!/usr/bin/python3
for ascii_value in range(97, 123):
    if chr(ascii_value) != 'e' and chr(ascii_value) != 'q':
        print(f'{chr(ascii_value)}', end='')
