#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    weights = sum(tuple([w[1] for w in my_list]))
    total = sum([i[0] * i[1] for i in my_list])
    weighted_average = total / weights
    return weighted_average
