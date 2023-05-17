#!/usr/bin/python3

def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        unique_values = set(my_list)
        sum = 0
        for value in unique_values:
            sum += value
        return sum
    return None
