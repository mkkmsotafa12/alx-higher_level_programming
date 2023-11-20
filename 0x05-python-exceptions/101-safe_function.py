#!/usr/bin/python3
import sys



def safe_function(fct, *args):



    try:
        ptr = fct(*args)
    except(BaseException) as p:
        ptr = None
        print("Exception: {}".format(p), file=sys.stderr)
    finally:
        return (ptr)

