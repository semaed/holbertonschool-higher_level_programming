#!/usr/bin/python3

def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and not a % 5 == 0:
            print("Fizz", end=" ")
        elif a % 5 == 0 and not a % 3 == 0:
            print("Buzz", end=" ")
        elif a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(a, end=" ")
