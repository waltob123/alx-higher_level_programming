#!/usr/bin/python3
'''10_square module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A class that defines a Square and inherits
    from the Rectangle class
    '''

    def __init__(self, size):
        '''
        Instatiates a Square

        Args:
            size(int): size of the square
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
