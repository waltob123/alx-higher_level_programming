#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for integer in my_list.reverse():
            print('{:d}'.format(integer))
