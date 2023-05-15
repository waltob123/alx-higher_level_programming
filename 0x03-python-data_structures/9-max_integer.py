#!/usr/bin/python3

def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) < 1:
            return None
        my_list.sort()
        return my_list[-1]
