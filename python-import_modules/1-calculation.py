#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    adding = add(a, b)
    print("{} + {} = {}".format(a, b, adding), end="\n")
    subs = sub(a, b)
    print("{} - {} = {}".format(a, b, subs), end="\n")
    mult = mul(a, b)
    print("{} * {} = {}".format(a, b, mult), end="\n")
    quotient = div(a, b)
    print("{} / {} = {}".foirmat(a, b, quotient), end="\n")
