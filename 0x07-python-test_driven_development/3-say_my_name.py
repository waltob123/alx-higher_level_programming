#!/usr/bin/python3
'''say my name module'''


def say_my_name(first_name, last_name=""):
    '''
    A function which prints your firstname and lastname
    together.

    Args:
        first_name(str)
        last_name(str)

    Return:
        None
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
