#!/usr/bin/python3
'''100-my_int module'''


class MyInt(int):
    '''A rebel class that inherits from int'''

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
