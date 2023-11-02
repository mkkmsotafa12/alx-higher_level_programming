#!/usr/bin/python3
def magic_calculation(a, b):

  # Improt add, sub function
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    # check if 'a' is less than 'b'
    if a < b:
        c = add(a, b)

    # Preform addtion using a loop
    for i in range(4, 6):
        c = add(c, i)

        return c
    else:
        return sub(a, b)
