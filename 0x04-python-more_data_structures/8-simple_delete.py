#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary['name']
