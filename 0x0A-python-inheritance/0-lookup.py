#!/usr/bin/python3
'''0_lookup module'''


def lookup(obj):
    '''
    A function to return the attributes and methods
    of an object.

    Args:
        obj(object): Object to lookup its attributes and methods

    Return:
        result(list): list of attributes and methods
    '''
    result = dir(obj)
    return result
