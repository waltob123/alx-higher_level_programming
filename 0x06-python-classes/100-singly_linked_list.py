#!/usr/bin/python3
'''Module singly linked list'''


class Node:
    '''
    This class defines a node of a singly linked list
    '''

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')

        if next_node is not None or not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''
    This class defines a singly linked list
    '''

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            tmp = self.__head
            while tmp is not None:
                if tmp.__next_node is None:
                    tmp.__next_node = new_node
                    new_node.__next_node = None
                if new_node.__data < tmp.__next_node.__data:
                    new_node.__next_node = tmp.__next_node
                    tmp.__next_node = new_node
                tmp = tmp.__next_node

    def __str__(self):
        result = ""
        tmp = self.__head
        while tmp is not None:
            result += str(self.data)
            result += '\n'
            tmp = tmp.__next_node
        return result
