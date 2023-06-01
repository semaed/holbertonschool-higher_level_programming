#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasdi = str(number)[-1:]
if lasdi > "5":
    if number < 0:
        print(
            f"Last digit of {number} is -{lasdi} and is less than 6 and not 0")
    else:
        print(
            f"Last digit of {number} is {lasdi} and is gretaer than 5")
elif lasdi == "0":
    print(f"Last digit of {number} is {lasdi} and is 0")
else:
    print(
        f"Last digit of {number} is {lasdi} and is less than 6 and not 0")
