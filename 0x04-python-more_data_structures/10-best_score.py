#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) < 1:
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda x: x[1])
    return sorted_dict[len(sorted_dict)-1][1]
