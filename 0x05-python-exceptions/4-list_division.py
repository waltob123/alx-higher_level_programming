#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    returning_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by zero')
        except IndexError:
            result = 0
            print('out of range')
        finally:
            returning_list.append(result)            
    return returning_list
