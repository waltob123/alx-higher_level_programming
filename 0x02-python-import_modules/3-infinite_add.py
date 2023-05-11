#!/usr/bin/python3
import sys


if __name__ == '__main__':
    sum = 0
    args_length = len(sys.argv)
    
    if args_length <= 1:
        sum = 0
        print('{}'.format(sum))
    elif args_length > 1:
        counter = 1
        while counter < args_length:
            sum += int(sys.argv[counter])
            counter += 1
        print('{}'.format(sum))
