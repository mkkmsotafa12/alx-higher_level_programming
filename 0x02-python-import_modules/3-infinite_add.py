#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = sys.argv[1:]
    sum_of_argc = 0
    for arg in argc:
        sum_of_argc += int(arg)
    print(sum_of_argc)
