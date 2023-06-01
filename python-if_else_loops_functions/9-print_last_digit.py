#!/usr/bin/python3
def print_last_digit(number):
    lasdi = abs(number) % 10
    print(lasdi, end="")
    return lasdi
