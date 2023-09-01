#!/usr/bin/python3
'''peak module'''


def find_peak(list_of_integers):
    '''
    finds the peak in an unsorted list of integers

    Args:
        list_of_integers (list): list to find peak from
    Return:
        peak (int)
    '''
    # return None if list is empty
    if len(list_of_integers) == 0 or list_of_integers == []:
        return None

    # return first element if list contains 1 element
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    # return maximum element if list contains 2 elements
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    # using binary search
    mid = len(list_of_integers) / 2  # get the middle element
    peak = list_of_integers[mid]  # set peak to the middle element
    # if peak is greater than it's neighbors return peak
    # else if peak is less than it's neigbors return find_peak
    if peak > list_of_integers[mid-1] and peak > list_of_integers[mid+1]:
        return peak
    elif peak < list_of_integers[mid-1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid+1:])
