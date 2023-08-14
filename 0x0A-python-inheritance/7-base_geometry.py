#!/usr/bin/python3
'''7_base_geometry module'''


class BaseGeometry:
    '''
    A class that defines a BaseGeometry
    '''

    def area(self):
        '''calculate the area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''check to see if value is an integer and greater than 0'''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
