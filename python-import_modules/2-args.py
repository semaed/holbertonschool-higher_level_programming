#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count == 0:
File is present

First line contains #!/usr/bin/python3

Your program should run only as script, not as imported module

Correct output - case: Hello

Correct output - case: Hello There

Correct output - case:

Correct output - case: 98 Battery street
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments: ".format(arg_count))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
