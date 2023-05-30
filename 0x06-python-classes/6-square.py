#!/usr/bin/python3
'''Module square'''


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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) > 2 or \
                (not all(value[0] >= 0, value[1] >= 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
