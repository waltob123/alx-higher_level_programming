#!/usr/bin/python3
'''2_is_same_class module'''


def is_same_class(obj, a_class):
    '''
    A function that returns True if the object passed
    to the function is an instance of the class passed to the function.
    Otherwise return False.

    Args:
        obj(object): objecet to check if it is an instance of a_class
        a_class(class): class to check obj against

    Return:
        True or False
    '''
    if isinstance(obj, a_class):
        return True
    return False
