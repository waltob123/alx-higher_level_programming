#!/usr/bin/python3
'''Rectangle Module'''


class Rectangle:
    '''A class that defines a rectangle

    Args:
        number_of_instances(int): public class attribute to count the number
                                    of instances created.
        width(int): width of the rectangle
        height(int): height of the rectangle
    '''

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        perimeter = None
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
            return perimeter
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self):
        '''prints an informal string of an instance'''
        if self.__width == 0 or self.__height == 0:
            return ''

        rect = []
        # for i in range(self.__height):
        #     rect.append(self.__width * '#')
        #     rect.append('\n')
        # return ''.join(rect)
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''returns a string representation of the class'''
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'

    def __del__(self):
        '''returns a string if an instance is deleted'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        comapares the area of two rectangles and returns the rectangle
        with the biggest area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        # check for the rectangle with the larges area
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
