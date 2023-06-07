#!/usr/bin/python3
'''print square module'''


def print_square(size):
    '''
    prints a square using #

    Args:
        size(int) - size of the square

    Return:
        None
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
