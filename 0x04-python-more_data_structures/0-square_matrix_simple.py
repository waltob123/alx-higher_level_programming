#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0 and isinstance(matrix, list):
        for array in matrix:
            if isinstance(array, list):
                new_matrix.append(list(map(lambda x: x * x, array)))
            else:
                continue
        return new_matrix
    return None
