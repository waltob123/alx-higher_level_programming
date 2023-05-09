#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for char in str:
        if ord(char) not in range(97, 123):
            new_str += char
        elif ord(char) in range(97, 123):
            new_str += chr(ord(char) - 32)
    print(new_str)
