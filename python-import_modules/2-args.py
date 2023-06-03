#!/usr/bin/python3

import sys
if __name__ == "__main__":

    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count), end="\n")
        print(f"{arg_count}:", "".join(args), end="\n")
    else:
        print("{} arguments: ".format(arg_count))
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}", end="\n")
