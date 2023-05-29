#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    returning_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            returning_list.append(result)
        except TypeError:
            result = 0
            returning_list.append(result)
            print('wrong type')
            continue
        except ZeroDivisionError:
            result = 0
            returning_list.append(result)
            print('division by zero')
            continue
        except IndexError:
            result = 0
            returning_list.append(result)
            print('out of range')
            continue
    return returning_list
