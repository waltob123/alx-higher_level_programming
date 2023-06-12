#!/usr/bin/python3
'''3_is_kind_of_class module'''


def is_kind_of_class(obj, a_class):
    '''
    A function to check if an object is an instance of a_class
    or is instance of the class inherited by a_class.

    Args:
        obj(object): Object to check against a_class
        a_class(class): class to check against obj

    Return:
        True or False
    '''
    if isinstance(obj, a_class) or issubclass(obj.__class__, a_class):
        return True
    return False
