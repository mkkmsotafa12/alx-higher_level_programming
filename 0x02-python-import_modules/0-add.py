#!/usr/bin/python3
def add(a, b):
    from add_0 import add

    # assign the value 1 to a variable called 'a'
    a = 1

    # assign the value 2 to a variable called 'b'
    b = 2

    # call the 'add' function from the 'add_0' module with 'a' and 'b' as arguments
    result = add(a, b)

    # print the formatted string showing the addtion result
    print("{} + {} = {}".format(a, b, result))
