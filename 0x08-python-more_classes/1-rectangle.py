#!/usr/bin/python3
'''Rectangle Module'''


class Rectangle:
    '''A class that defines a rectangle

    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    '''

    def __init__(self, width=0, height=0):
        '''initiliazes an object with height and width for the rectangle'''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''returns the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''returns the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
