#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args_length = len(sys.argv) - 1
    
    if args_length == 1:
        print('{} argument:'.format(args_length))
    elif args_length == 0:
        print('{} arguments.'.format(args_length))
    elif args_length > 1:
        print('{} arguments:'.format(args_length))
    
    for counter in range(args_length):
        print('{}: {}'.format(counter + 1, sys.argv[counter + 1]))
