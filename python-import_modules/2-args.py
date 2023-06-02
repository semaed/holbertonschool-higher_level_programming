#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments: ".format(arg_count))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
