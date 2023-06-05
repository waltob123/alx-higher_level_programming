#!/usr/bin/python3
'''Rectangle Module'''


class Rectangle:
    '''
    A class that defines a rectangle

    args: width - width of the rectangle
          height - height of the rectangle

    default_values: width=0, height=0
    '''

    def __init__(self, width=0, height=0):
        '''
        Constructor method to initialize width and hieght
        anytime an object of the rectangle class is created
        '''

        # check if width is integer
        if not isinstance(width, int):
            raise TypeError(f'width must be an integer')
        # check if height is integer
        if not isinstance(height, int):
            raise TypeError(f'height must be an integer')
        # check if width is greater than 0
        if width < 0:
            raise ValueError('width must be >= 0')
        # check if width is greater than 0
        if height < 0:
            raise ValueError('height must be >= 0')
        self.width = width
        self.height = height

        @property
        def width(self):
            '''property to get width of rectangle'''
            return self.__width

        @width.setter
        def width(self, value):
            '''property to set the value of width of rectangle'''
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            '''property to get height of rectangle'''
            return self.__height

        @height.setter
        def height(self, value):
            '''property to set the value of height of rectangle'''
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
