#!/usr/bin/python3
i = 122

while (i >= 65 and i < 91) or (i > 96 and i < 123):
    print(chr(i), end='')
    if i > 96 and i < 123:
        i = i - 33
    elif i > 64 and i < 91:
        i = i + 31
