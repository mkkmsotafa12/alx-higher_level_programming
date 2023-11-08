#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
        if my_list is None:
            return (None)
        if len(my_list) == 0:
            return ([])
        for c in my_list:
            if c == search:
            new_list.append(replace)
        else:
            new_list.append(c)
            return (new_list)

