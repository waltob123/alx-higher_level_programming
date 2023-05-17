#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new_list = [x for x in my_list]
        for item in range(len(new_list)):
            if new_list[item] == search:
                new_list[item] = replace
        return new_list
    return None
