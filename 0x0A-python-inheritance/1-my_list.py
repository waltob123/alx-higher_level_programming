#!/usr/bin/python3
'''1_my_list module'''


class MyList(list):
    '''A class that inherits from the list class'''

    def print_sorted(self):
        '''prints list items in ascending order'''
        print(sorted(self))
