#!/usr/bin/python3
'''4_inherits_from module'''


def inherits_from(obj, a_class):
    '''
    A function to check if an object is inherited directly
    or indirectly from a class.

    Args:
        obj(object): Object to check against a_class
        a_class(class): Class to check against obj
    '''
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
