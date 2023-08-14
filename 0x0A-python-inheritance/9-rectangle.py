#!/usr/bin/python3
'''8_rectangle module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    A class that defines a Rectangle and inherits from the
    BaseGeometry class
    '''

    def __init__(self, width, height):
        '''
        Initializes a new Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''calculates the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
