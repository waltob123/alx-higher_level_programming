#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        if idx < 0 or idx > (len(my_list) - 1):
            return my_list
        del my_list[idx]