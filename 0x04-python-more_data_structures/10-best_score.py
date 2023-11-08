#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    biggest = 0
    biggest_key = ""
    for i in a_dictionary:
        if a_dictionary[i] > biggest:
            biggest = a_dictionary[i]
            biggest_key = i
    return (biggest_key)
