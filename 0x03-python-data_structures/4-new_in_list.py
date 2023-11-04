#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list


    my_copy_list = my_list.copy()
    my_copy_list[idx] = element
    return my_copy_list
