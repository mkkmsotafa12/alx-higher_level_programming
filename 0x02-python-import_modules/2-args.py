#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = sys.argv[1:]

    num_argc = len(argc)

    if num_argc == 0:
        print("0 arguments.")
    elif num_argc == 1:
        print ("1 arguments.")
    else:
        print("{} arguments:".format(num_argc))

    for i, arg in enumerate(argc):
        print("{}: {}".format(i + 1, arg))
