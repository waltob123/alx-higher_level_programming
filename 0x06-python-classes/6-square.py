#!/usr/bin/python3

class Square():
    '''
    This is a python class that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple) or len(position) > 2 or \
                (not all(position[0] >= 0, position[1] >= 0)):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
