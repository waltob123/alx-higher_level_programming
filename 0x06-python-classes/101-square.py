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

        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(position[0], int) or not \
                isinstance(position[1], int):
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
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """
        Prints the square forming by '#' symbol
        """
        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    def __str__(self):
        string = ""
        if self.__size == 0:
            return "\n"

        string += '\n'*self.__position[1]
        for i in range(self.__size):
            string += ' '*self.__position[0]
            string += '#'*self.__size
            if i is not self.__size - 1:
                string += '\n'
        return string
