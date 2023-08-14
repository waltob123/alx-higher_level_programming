#!/usr/bin/python3
'''matrix divided module'''


def matrix_divided(matrix, div):
    '''Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int|float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    '''

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if not isinstance(matrix, list) or not \
            all([isinstance(row, list) for row in matrix]) or not \
            all(list(map(lambda x: isinstance(x, int) or
                isinstance(x, float),
                [i for row in matrix for i in row]))) or not \
            all([len(row) > 0 for row in matrix]):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    if not all([len(row) == len(matrix[0]) for row in matrix]):
        raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(new_row)
    return new_matrix
